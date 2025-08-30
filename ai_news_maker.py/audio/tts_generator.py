import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_audio(API_KEY,text):
    url = "https://api.v8.unrealspeech.com/stream"
    headers = {
         "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
      "Text": (
          text
        ),
        "VoiceId": "Noah",
        "Bitrate": "192k",
        "Pitch": 1.02,
        "Speed": 0.1
    }

    response = requests.post(url, headers=headers, json=data,verify = False)

    if response.status_code == 200:
        with open("output.mp3", "wb") as f:
            f.write(response.content)
        print(" Audio saved as output.mp3")
    else:
      print(" Error:", response.status_code, response.text)