import google.generativeai as palm
from config import PALM_API_KEY

palm.configure(api_key=PALM_API_KEY)

defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.7,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
    'max_output_tokens': 1024,
    'stop_sequences': [],
    'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
}

def strict_output(prompt):
    res = palm.generate_text(
        **defaults,
        prompt=f"{prompt}"
    )
    return res

def advanced_output(prompt):
    res = palm.generate_text(
        **defaults,
        prompt=f"{prompt} with chapters {prompt} also generate 5 questions and quiz to complete afte each video."
    )
    return res