import requests


url = "http://127.0.0.1:8000/api/method/librify.APIS.People.get_people"



headers = {
    "Authorization":"token 59278c28b558cc4:6f55f7469e80f3e",
    "Content_type":"application/json"
}


response = requests.get(url,headers=headers)


if response.status_code ==200:
    print("Successfully geting the data:",response.json())

else:
    print("Not geeting successfully")