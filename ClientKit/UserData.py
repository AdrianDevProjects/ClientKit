import requests

def get_user_name(userid):
    url = "https://onlineservices.adriandevprojects.com/v1/user/get/username/"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "userid": userid
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        data = response.json()
        username = data['username']
        return username
    else:
        return response.status_code