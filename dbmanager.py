from datetime import datetime
from chromadb import PersistentClient
from logger_config import logger

class ChromaDBManager:
    def __init__(self, db_path="data/vector", collection_name="mistakes_db"):
        """Initialize the ChromaDB client and collection."""
        self.client = PersistentClient(db_path)
        self.collection_name = collection_name
        self.collection = self.client.get_or_create_collection(name=self.collection_name)

    def insert_data(self, data):
        """Insert multiple entries into the ChromaDB collection."""
        for entry in data:
            document = entry['mistake']
            metadata = {
                'timestamp': entry['timestamp'],
                'original_text': entry['original_text'],
                'corrected_text': entry['corrected_text'],
                'involved_words': str(entry['involved_words']),
                'vocabulary': str(entry['vocabulary']),
                'mispronounced': str(entry['mispronounced'])
            }
            self.collection.add(
                ids=[str(entry['id'])],
                documents=[document],
                metadatas=[metadata]
            )
        logger.info(f"Data successfully inserted into the collection: {self.collection_name}")

    def query_data(self, query_text, top_k=5):
        """Query the collection for relevant entries based on input text."""
        query_result = self.collection.query(
            query_texts=[query_text],
            n_results=top_k
        )
        result = ""
        for doc, metadata in zip(query_result["documents"][0], query_result["metadatas"][0]):
            result += f"Grammar mistake: {doc}\n"
            result += f"Original Text: {metadata['original_text']}\n"
            result += f"Corrected Text: {metadata['corrected_text']}\n"
            result += f"Involved Words: {metadata['involved_words']}\n"
            result += f"Vocabulary Suggestion: {metadata['vocabulary']}\n"
            result += f"Mispronounced Words: {metadata['mispronounced']}\n\n"

        logger.info(f"Query results for '{query_text}': {result}")

        return result, query_result["ids"][0]


    def update_document(self, doc_id, new_document, new_metadata=None):
        """Update the content or metadata of an existing document."""
        self.collection.update(
            ids=[doc_id],
            documents=[new_document],
            metadatas=[new_metadata] if new_metadata else [{}]
        )
        logger.info(f"Document with ID {doc_id} successfully updated.")

    def delete_document(self, doc_id):
        """Delete a document from the collection using its ID."""
        self.collection.delete(ids=[doc_id])
        logger.info(f"Document with ID {doc_id} successfully deleted.")


    def get_document_by_id(self, doc_id):
        """Retrieve a document by its ID."""
        result = self.collection.get(ids=[doc_id])
        return result

    def get_most_recent_entry(self):
        """Retrieve the most recent entry based on the timestamp."""
        # Get all documents and their metadata
        all_documents = self.collection.get()
        if not all_documents["documents"]:
            return "No documents found in the collection."

        # Combine documents and metadata for easy sorting
        combined_data = list(zip(all_documents["documents"], all_documents["metadatas"], all_documents["ids"]))

        # Correct the format to match the actual timestamp format
        sorted_data = sorted(combined_data, key=lambda x: datetime.strptime(x[1]['timestamp'], "%Y-%m-%d %H:%M:%S"),
                             reverse=True)

        # Get the most recent document
        most_recent_document, most_recent_metadata, most_recent_id = sorted_data[0]

        result = ""
        result += f"mistake: {most_recent_document}\n"
        result += f"Original Text: {most_recent_metadata['original_text']}\n"
        result += f"Corrected Text: {most_recent_metadata['corrected_text']}\n"
        result += f"Involved Words: {most_recent_metadata['involved_words']}\n"
        result += f"Vocabulary: {most_recent_metadata['vocabulary']}\n"
        result += f"Mispronounced Words: {most_recent_metadata['mispronounced']}\n"

        logger.info(f"Retrieved most recent entry: {result}")

        return result, [most_recent_id]

