import requests
from PIL import Image
from io import BytesIO
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_images(API_KEY,topic_list):
    images = []
    try:
        for topic in topic_list:
            url = f"https://api.unsplash.com/search/photos?query={topic}&per_page=5&client_id={API_KEY}"
            response = requests.get(url,verify=False)
            if response.status_code == 200:
                #getting image url
                photos = response.json()
                photo = photos['results'][0]
                image_url = photo['urls']['regular']

                res = requests.get(image_url)
                if res.status_code == 200:
                    img = Image.open(BytesIO(res.content))  # Convert bytes to PIL image
                    images.append(img)  # Store in list
                else:
                    print("Failed to download image")
        return images
    except Exception as e:
       print(f"Unexpected Error:{e}")
