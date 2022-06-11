import requests

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
print(response.status_code)

response1 = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
print(response1.status_code)

first_response = response1.history[0]
second_response = response1

print(first_response.url)
print(second_response.url)
