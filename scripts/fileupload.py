import requests


base_url = "http://127.0.0:8000/api/method/upload_file"

headers = {
    "authorization":"token 59278c28b558cc4:11a25271783cc96",
    "Content_type":"application/json"
}


files={
    "file":open("binary.bin","rb")
}


data={
    "is_private":1,
    "doctype":"Person",
    "docname":"PR-00011"
}


response = requests.post(base_url,headers=headers,files=files,data=data)

if response.status_code==200:
    print("Successfully file uploaded:",response.json())
else:
    print("Not uploaded",response.status_code)