import requests
from send_email_news import send_email

topic = "tesla"
api_key = "1c431b8cedcb41b38c1bebca567a6a86"
url = "https://newsapi.org/v2/everything?" \
      "q={}&" \
      "sortBy=publishedAt&" \
      "apiKey={}&" \
      "language=en".format(topic, api_key)



# url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=1c431b8cedcb41b38c1bebca567a6a86&language=en"

request = requests.get(url)
content = request.json()


body = "Subject: Today's news" + "\n"
for article in content["articles"][:20]:
    if (article["description"] is not None) and (article["title"] is not None):
        body = body + article["title"] + "\n"\
               + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
