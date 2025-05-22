from dbmanager import ChromaDBManager
from logger_config import logger
import json
from analysis_dict import GrammarMistake
from user_dict import UserProfile
from prompts import default_prompt


class ExerciseGenerator:
    def __init__(self, db: ChromaDBManager, llm, user_profile: UserProfile):
        self.db = db
        self.llm = llm
        self.user_profile = user_profile

    def generate_exercise(self, current_analysis: GrammarMistake = None):
        if current_analysis is None:
            old_utterances, ids = self.db.get_most_recent_entry()

            # Cold start
            if old_utterances is None or not old_utterances:
                logger.info("Cold start, creating exercise without any context from previous mistakes")
                exercise = self.llm.complete(default_prompt.format(user_profile=self.user_profile,
                                                                   current_analysis=None, old_utterances=None))
            else:
                exercise = self.llm.complete(default_prompt.format(user_profile=self.user_profile,
                                                                   current_analysis=None,
                                                                   old_utterances=old_utterances))
        else:
            old_utterances, ids = self.db.query_data(current_analysis.mistake, top_k=2)

            # Cold start
            if old_utterances is None or not old_utterances:
                logger.info("Cold start, creating exercise without any context from the database")
                exercise = self.llm.complete(default_prompt.format(user_profile=self.user_profile,
                                                                   current_analysis=current_analysis,
                                                                   old_utterances=None))
            else:
                exercise = self.llm.complete(default_prompt.format(user_profile=self.user_profile,
                                                                   current_analysis=current_analysis,
                                                                   old_utterances=old_utterances))

        # The below part is how we keep in sync with the changing user behaviour
        if current_analysis:
            self.db.insert_data([current_analysis.to_dict()])

        if ids:
            for id in ids:
                self.db.delete_document(id)

        return exercise

    def multimodal_transform(self, exercise):
        ex = json.loads(exercise)
        theme = ex.get("theme", "default")  # Use 'default' if theme is not found

        result = f"{exercise}\nImage: <insert {theme}.jpg>"
        return result
