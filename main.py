import requests
from send_email_news import send_email

api_key = "1c431b8cedcb41b38c1bebca567a6a86"
# url = "https://newsapi.org/v2/everything? \
# 	q=dell& \
# 	sortBy=publishedAt& \
# 	apiKey=1c431b8cedcb41b38c1bebca567a6a86 \
# 	language=en"

url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=1c431b8cedcb41b38c1bebca567a6a86&language=en"

request = requests.get(url)
content = request.json()


body = ""
for article in content["articles"]:
	if article["title"] and article["description"] is not None:
		body = body + article["title"] + "\n" + article["description"] + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
