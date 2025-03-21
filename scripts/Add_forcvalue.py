import requests


url_base = "http://127.0.0.1:8000"
endpoint = "/api/resource/forgetvalue"


headers = {
    "Authorization":"token 59278c28b558cc4:d5162811ea598de",
    "Content_type":"application/json"
}


response = requests.get(url_base+endpoint,headers=headers)


if response.status_code ==200:
    data = response.json()
    print(data)

else:
    print("Data is not Geting")