import requests


base_url = "http://127.0.0.1:8000"
endpoint = "/api/resource/Person"

params = {
    "filters": '[["gender","=","male"]]'
}


headers = {
    "Authorization":"token 59278c28b558cc4:b3d52070c2f2ed6",
    "Content-type":"application/json"
}


response = requests.get(base_url+endpoint,headers = headers,params=params)
if response.status_code==200:
    print("DIaplying the Records")
    print(response.json())
else:
    print("Not Applicable")
