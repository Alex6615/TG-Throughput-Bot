import json
import requests



def Get_Wking_UserCount():
    session = requests.session()
    headers = {
        'Accept' : 'application/json',
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer glsa_qOHsDNPG4z8Hr87LlXgpBzQokb91s2Xn_79ffa6a3'   
    }
    #response = session.get('https://wking-users.owin.info/api/User/onlineusers', headers = headers, verify=False)
    response = session.get('http://192.168.82.160:30196/api/User/onlineusers', headers = headers, verify=False)
    user_count = json.loads(response.content).split()[-1]
    session.close()
    return user_count


if __name__ == "__main__" :
    pass