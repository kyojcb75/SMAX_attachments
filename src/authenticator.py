import requests


def get_token():
    try:

        url = "https://sma-csc.itstk.com/auth/authentication-endpoint/authenticate/login"
        querystring = {
            "TENANTID": "716383812"
        }
        payload = "{\"Login\": \"jonathan\",\"Password\": \"Jonathan2022*_\"}"
        headers = {
            'Content-Type': "application/json",
        }

        response = requests.request("POST", url, data=payload, headers=headers, params=querystring, verify=False)

        return response.text


    except Exception as e:
        print("fallo en metodo getToken()")
        print(e)
