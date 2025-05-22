from chromadb import PersistentClient
import json
from logger_config import logger


def load_data(datapath, db:PersistentClient):
    """Load data from a JSON file and insert it into the ChromaDB collection if it is empty."""
    all_documents = db.collection.get()

    if all_documents["documents"]:
        logger.info(f"The collection '{db.collection_name}' already contains data. Loading aborted.")
        return

    with open(datapath) as f:
        data = json.load(f)

    db.insert_data(data)
    logger.info(f"Data successfully loaded from {datapath} and inserted into the collection: {db.collection_name}")
