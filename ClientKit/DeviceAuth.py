import requests



def request_auth():
    auth_url = "https://onlineservices.adriandevprojects.com/v1/auth/devicelogin/new/"


    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(auth_url, headers=headers)

    print(response.text)