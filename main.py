import requests

url = "https://finance.yahoo.com/"

request = requests.get(url)
content = request.text

print(content)
