import requests
import json
base_url= "http://127.0.0.1:8000"
end_point = "/api/resource/Person"


headers = {
   "Authorization":"token 59278c28b558cc4:6f55f7469e80f3e",
   "Content-Type":"application/json"
}


data = {
    "fname":"Srushti",
    "sname":"Mehta",
    "age":9
}
response = requests.post(base_url+end_point,headers=headers,data=json.dumps(data))


if response.status_code == 200:
    print("Congratulation New Person is Just Added our Team!")
    print(response.json())

else:
    print("Person is not Added Successfully")