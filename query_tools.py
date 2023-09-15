import json
import requests
try :
    from secret_account import wking_api
except :
    from secret_account_local import wking_api
from urllib3.exceptions import InsecureRequestWarning

# Ref: https://stackoverflow.com/questions/15445981/how-do-i-disable-the-security-certificate-check-in-python-requests
# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

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