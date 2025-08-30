import requests

def get_latest_headlines(API_KEY):

    url_news = (
        'https://newsapi.org/v2/top-headlines?'
        'sources=bbc-news&'
        f'apiKey={API_KEY}'
    )

    try:
        response = requests.get(url_news,timeout=20)
        response.raise_for_status()

        data = response.json()

        if data.get('status') == 'ok' and data.get('articles'):
            article = data['articles'] 
            return (article[0]["title"],article[0]["description"])
        else:
            return None
            print("No articles found or API returned an error.")
    #for requests, timeout realted error
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
    #for handling all types of error
    except Exception as e:
        print(f"Unexpected error: {e}")