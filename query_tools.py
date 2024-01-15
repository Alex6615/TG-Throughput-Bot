import json
import requests
try :
    from secret_account import wking_api, dobet_api
except :
    from secrets.secret_account_local import wking_api, dobet_api
from urllib3.exceptions import InsecureRequestWarning

# Ref: https://stackoverflow.com/questions/15445981/how-do-i-disable-the-security-certificate-check-in-python-requests
# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


class UserGetter :
    def __init__(self, serverId):
        self.session = requests.session()
        self.headers = {
            'Accept' : 'application/json',
            'Content-Type' : 'application/json',
        }
        if serverId == 9 :
            self.target = wking_api
            self.site = "Wking"
        elif serverId == 103 :
            self.target = dobet_api
            self.site = "Dobet"
        else :
            pass

    def Get_UserCount(self):
        response = self.session.get(self.target, headers = self.headers, verify=False)
        user_count = json.loads(response.content).split()[-1]
        reply_text = f"🌏 <b> {self.site} Online Users Now : </b><code>{user_count}</code>"
        return reply_text
    
    def __del__(self):
        self.session.close()

if __name__ == "__main__" :
    x = "9"
    defx = f"Get_{x}_UserCount"
    x = defx()
    print(x)