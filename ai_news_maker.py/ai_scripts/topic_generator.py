import requests
import google.generativeai as genai


def get_topics(API_KEY,script):
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')

        prompt = f'''See I am making ai news maker so i want stock photos for it ,
                    so I want you to convert the given script of 1 min  into 20 different
                    main topics(make the topics short and concise) , sequentially , seperated by commas
                    and the script is = {script}'''
        topic = model.generate_content(prompt)
        var = topic.text.split(',')
        return var
    except Exception as e:
        print((f"Unexpected Error: {e}"))