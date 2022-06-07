import requests

response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1": "valueq1"})
response1 = requests.post("https://playground.learnqa.ru/api/check_type", params={"param1": "valueq1"})
response2 = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "valueq1"})

print(1, response.text)
print(2, response1.text)
print(3, response2.text)
