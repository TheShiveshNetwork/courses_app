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
    system_prompt = "You are an AI capable of curating course content, coming up with relevant chapter titles, and finding relevant online articles/available youtube videos for each chapter"
    concluding_prompt = "Make sure that the links are working fine. The response should be in markdown format, with headings, links, and text description."
    res = palm.generate_text(
        **defaults,
        prompt=f"{system_prompt}. The title of the course is {prompt}, create relevant chapter titles for this topic and provide online articles/available youtube videos link for it. {concluding_prompt}"
    )
    return res

def advanced_output(prompt, list):
    system_prompt = "You are an AI capable of curating course content, coming up with relevant chapter titles, and finding relevant online articles/available youtube videos for each chapter"
    units_prompt = f"It is your job to create a course about all the chapter mentioned in the unit list as {list}. The user has requested to create chapters for each of the units. Then, for each chapter, provide a detailed youtube search query that can be used to find an informative educational video for each chapter. Each query should give an educational informative course in youtube."
    concluding_prompt = "Make sure that the links are working fine. The response should be in markdown format, with headings, links, and text description."
    res = palm.generate_text(
        **defaults,
        prompt=f"{system_prompt}. The title of the course is {prompt}. {units_prompt}. {concluding_prompt}"
    )
    return res