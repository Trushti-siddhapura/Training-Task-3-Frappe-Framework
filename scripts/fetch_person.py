import requests

base_url = "http://127.0.0.1:8000"
api_endpoint = "/api/resource/Person/PR-00010"


headers = {
    "Authorization": "token 59278c28b558cc4:31da1531db843f0",
    "Content-Type": "application/json"
}


response = requests.delete(base_url + api_endpoint, headers=headers)
if response.status_code == 200:
    print("Successfully Deleted")
else:
    print("Error: Empty response received")