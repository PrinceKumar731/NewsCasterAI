from config import UNREAL_SPEECH_API_KEY
from config import NEWS_API_KEY
from config import GEMINI_API_KEY
from config import UNSPLASH_ACCESS_KEY
import time

from audio.tts_generator import get_audio
from news.news_api import get_latest_headlines
from ai_scripts.script_generator import get_script
from ai_scripts.topic_generator import get_topics
from images.image_fetcher import get_images
from video.video import get_video
from youtube.upload_video import upload_video

title,description = get_latest_headlines(NEWS_API_KEY)

text = get_script(GEMINI_API_KEY,title,description)

text = text[:988]
print(text)

topic_list=get_topics (GEMINI_API_KEY,text)

image = get_images(UNSPLASH_ACCESS_KEY,topic_list)
print("***IMAGES GENERATED***")

get_audio(UNREAL_SPEECH_API_KEY,text)
print("**Audio Generated***")

time.sleep(2)

get_video(image)
print("***Video Generated***")

upload_video(title, description)
