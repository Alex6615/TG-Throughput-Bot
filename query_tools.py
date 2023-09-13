import json
import requests
try :
    from secret_account import wking_api
except :
    from secret_account_local import wking_api


def Get_Wking_UserCount():
    session = requests.session()
    headers = {
        'Accept' : 'application/json',
        'Content-Type' : 'application/json',
    }
    response = session.get(wking_api, headers = headers, verify=False)
    
    user_count = json.loads(response.content).split()[-1]
    session.close()
    return user_count


if __name__ == "__main__" :
    x = Get_Wking_UserCount()
    print(x)