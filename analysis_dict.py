import uuid
from datetime import datetime
import json

class GrammarMistake:
    def __init__(self, mistake, original_text, corrected_text, involved_words, vocabulary, mispronounced, id=None, timestamp=None):
        self.id = id if id else str(uuid.uuid4())
        self.timestamp = timestamp if timestamp else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.mistake = mistake
        self.original_text = original_text
        self.corrected_text = corrected_text
        self.involved_words = involved_words
        self.vocabulary = vocabulary
        self.mispronounced = mispronounced

    def __str__(self):
        return f"ID: {self.id}\n" \
               f"Timestamp: {self.timestamp}\n" \
               f"Grammar Mistake: {self.mistake}\n" \
               f"Original Text: {self.original_text}\n" \
               f"Corrected Text: {self.corrected_text}\n" \
               f"Involved Words: {', '.join(self.involved_words)}\n" \
               f"Vocabulary: {self.vocabulary}\n" \
               f"Mispronounced Words: {', '.join(self.mispronounced)}"

    def to_dict(self):
        """
        Returns the GrammarMistake instance as a dictionary.
        """
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "mistake": self.mistake,
            "original_text": self.original_text,
            "corrected_text": self.corrected_text,
            "involved_words": self.involved_words,
            "vocabulary": self.vocabulary,
            "mispronounced": self.mispronounced
        }




