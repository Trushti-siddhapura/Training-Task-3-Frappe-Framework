import requests

base_url = "http://127.0.0.1:8000/api/method/login"


data = {
    "usr": "Administrator",  
    "pwd": "root"  
}          


session = requests.Session()

response = session.post(base_url,data)


if response.status_code == 200:
    # data = 
    print("login Successfully")
else:
    print("Error: Empty response received", response.status_code)


fetch_url = "http://127.0.0.1:8000/api/resource/Person"


response = session.get(fetch_url)


if response.status_code ==200:
    print(response.json())
else:
    print("Error fetching data:",response.status_code)