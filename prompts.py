

default_prompt = """
Create a personalized language learning exercise based on the following information:

1. Current Utterance Analysis:
   {current_analysis}

2. Past Mistakes:
   {old_utterances}

3. User Profile:
   {user_profile}

Follow these guidelines to create an effective exercise:

1. Always base the exercise on the current and past mistakes of the user. Make the user repeat the words they have 
mispronounced or misused in the exercise. Make the user use words that were previously suggested for vocabulary improvement.
 
2. Grammar (Explicit focus):
   - Target the grammar mistake from the current utterance or a similar one from past utterances.

3. Pronunciation (Implicit focus):
   - Include words the user has mispronounced (current or past) in the correct answer.

4. Vocabulary (Implicit focus):
   - Introduce new vocabulary or enhance existing words based on suggestions from current and past utterances.

5. Fluency (Implicit focus):
   - Design the exercise to encourage the user to utter a complete 'chunk' or 'paragraph' in a guided manner.
   

Exercise Structure:
- Create a fill-in-the-blanks exercise with a sentence or short paragraph.
- Provide 4 options (A, B, C, and D) for the blank.
- Ensure the correct option adheres to all 5 rules mentioned above.
- The correct answer should be a phrase or a sentence that has words the user struggles with, and has new vocabulary as 
per previous suggestions. Avoid single-word answers.
- The question should nudge the user into pronouncing the words they have mispronounced in the past.

Personalization:
- Incorporate the user's interests (e.g., favorite TV show, book, or hobby) into the exercise theme or content.

Output the exercise in the following JSON format:

{{
  "question": <The question with ____ for the blank phrase>,   
  "theme" : <A single entity among the user's favorite movie, book, hobby, etc>,   
  "intended_mistake" : <What mistake is the exercise trying to correct>,               
  "options": [                             
    {{
      "text": <The phrase pertaining to this option>,                     
      "is_correct": <True/False>               
    }}
  ]
}}

Ensure that your response contains only the JSON object with no additional text or explanations. Do not start with ```json
"""