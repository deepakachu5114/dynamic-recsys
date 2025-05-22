from analysis_dict import  GrammarMistake
from user_dict import UserProfile
from generator import ExerciseGenerator
from llama_index.llms.openai import OpenAI
from dbmanager import ChromaDBManager
from utils import load_data


# We create a db for our user
db = ChromaDBManager()
llm = OpenAI(api_key= "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", model="gpt-4o")

# loading the dummy data into vector db
# load_data("data/grammar.json", db)

# Creating an instance of the UserProfile
user_profile_instance = UserProfile(
    user_id="001",
    name="Deepak B",
    age=28,
    nationality="Indian",
    language_level="intermediate",
    favorite_movies=["Harry Potter", "Inception", "The Lord of the Rings"],
    favorite_books=["The Hobbit", "Pride and Prejudice", "Harry Potter Series"],
    favorite_tv_shows=["Friends", "Stranger Things", "Breaking Bad"],
    hobbies=["painting", "hiking", "photography"],
    favorite_artists=["Taylor Swift", "Adele", "Ed Sheeran"],
    favorite_songs=["Love Story", "Shape of You", "Rolling in the Deep"]
)

# Creating an instance of the ExerciseGenerator for the specific user
generator = ExerciseGenerator(
    db=db,
    llm=llm,
    user_profile=user_profile_instance
)

########################################################################################################################
# Few mistake instances to test the pipeline

mistake_instance = GrammarMistake(
    mistake="Incorrect use of articles",
    original_text="She is an best friend.",
    corrected_text="She is a best friend.",
    involved_words=["an", "a"],
    vocabulary={"best": "closest", "friend": "companion"},
    mispronounced=["best", "friend"]
)

mistake_instance1 = GrammarMistake(
    mistake="Subject-verb agreement error",
    original_text="The team are playing well.",
    corrected_text="The team is playing well.",
    involved_words=["are", "is"],
    vocabulary={"team": "squad", "playing": "performing"},
    mispronounced=["playing"]
)

# Instance 2: Incorrect Preposition Usage
mistake_instance2 = GrammarMistake(
    mistake="Incorrect preposition usage",
    original_text="I'm excited for go to the party.",
    corrected_text="I'm excited to go to the party.",
    involved_words=["for", "to"],
    vocabulary={"excited": "thrilled", "party": "celebration"},
    mispronounced=["excited", "party"]
)

# Instance 3: Incorrect Verb Tense
mistake_instance3 = GrammarMistake(
    mistake="Incorrect verb tense",
    original_text="Yesterday, I eat dinner at 8 PM.",
    corrected_text="Yesterday, I ate dinner at 8 PM.",
    involved_words=["eat", "ate"],
    vocabulary={"dinner": "supper", "yesterday": "the day before"},
    mispronounced=["yesterday", "dinner"]
)
########################################################################################################################



# This generates the exercise based on the mistake instance and the previous mistakes
exercise = generator.generate_exercise(mistake_instance2)
# This attaches an image pertaining to the theme of the exercise (dummy function, just to show the usage)
multimodal_exercise = generator.multimodal_transform(exercise.text)

print(multimodal_exercise)