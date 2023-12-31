import requests
import os

try :
    from secret_telegram import TELEGRAM_TOKEN, Notify_Group, MY_Group
except :
    from secrets.secret_telegram_local import TELEGRAM_TOKEN, Notify_Group, MY_Group
from query_tools import *



def SendPhoto(photo_name):
    if len(photo_name) == 0 :
        return 
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto?chat_id={Notify_Group}"
    # url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto?chat_id={MY_Group}"
    pwd = os.getcwd()
    file = f"{pwd}/resized_png/{photo_name}"
    files = {
        'photo': open(file, 'rb')
    }
    req = requests.post(url = url, files = files)
    req.close()


def SendText(text:str):
    if len(text) == 0 :
        return 
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={Notify_Group}&text={text}&parseMode=html"
    # url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={MY_Group}&text={text}&parseMode=html"
    req = requests.post(url = url)
    req.close()

if __name__ == "__main__" :
    pass