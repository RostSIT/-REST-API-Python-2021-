import requests

response = requests.get("https://playgroun.learnqa.ru/api/hello")
print(response.text)
