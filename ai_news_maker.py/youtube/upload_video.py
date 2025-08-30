from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

def upload_video(title, description):
    try:
        SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

        flow = InstalledAppFlow.from_client_secrets_file(
            r"C:\Users\Prince Kumar\Desktop\coding\api\ai_news_maker.py\youtube\client.json",
             SCOPES
        )
        creds = flow.run_local_server(port=0)

        youtube = build("youtube", "v3", credentials=creds)

        video_file = os.path.join(os.path.dirname(__file__), "..", "..", "shorts_video.mp4")
        video_file = os.path.abspath(video_file)

        if not os.path.exists(video_file):
            raise FileNotFoundError(f"Video file not found: {video_file}")

        request = youtube.videos().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": title,
                    "description": description,
                    "categoryId": "22"  
                },
                "status": {"privacyStatus": "public"} 
            },
            media_body=MediaFileUpload(video_file)
        )

        response = request.execute()
        print("Upload successful! Video ID:", response["id"])

    except FileNotFoundError as fnf_err:
        print("File error:", fnf_err)
    except Exception as e:
        print("An error occurred during upload:", e)
