import requests
import google.generativeai as genai

def get_script(API_KEY,topic,description):
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = (
        "This prompt is direct, gives clear negative constraints (what not to do), "
        "and tells the model exactly where to start.\n\n"
        f"Generate a script for a 1-minute explainer video on the topic={topic} and the description={description} which I have provided at the end of the prompt.\n\n"
        "CRITICAL INSTRUCTIONS:\n"
        "***MOST IMPORTANT:KEEP IT UNDER 700 WORDS"
        "Keep it short and concise"
        "Do not give any acts like close-up shots, just give the voiceover part.\n"
        "Do not include a title, character list, or scene settings.\n"
        "Do not make it boring, keep it interesting.\n"
        "Do not give background status such as wind roaring, calm environment\n"
        "Just give the content that need to be spoken\n"
        "Do not write any introductory or concluding phrases like \"Here is your script\" or \"I hope this helps.\"\n\n"
        "The response must begin directly with the first line of dialogue or the first action line "
        "and end with the last one. The output must be only the raw script text. This is the topic: "
    )

    try:
        info = model.generate_content(prompt)
        print('I AM WORKING')
        return info.text 
    except Exception as e:
        print(f"Error generating script: {e}")