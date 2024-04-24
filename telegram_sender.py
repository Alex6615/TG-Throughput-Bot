import requests
import os

try :
    from secret_telegram import TELEGRAM_TOKEN, Notify_Group, MY_Group, Top10Alert
except :
    from secrets.secret_telegram_local import TELEGRAM_TOKEN, Notify_Group, MY_Group, Top10Alert
from query_tools import *


tgThreadMapping = {
    # CdnServerId(int) : Topic(int),
    1 : 1,
}

def SendPhoto(photo_name, serverId, text:str="test"):
    if len(photo_name) == 0 :
        return 
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto?chat_id={Top10Alert}&message_thread_id={tgThreadMapping[serverId]}&caption={text}&parse_mode=html"
    pwd = os.getcwd()
    file = f"{pwd}/resized_png/{photo_name}"
    files = {
        'photo': open(file, 'rb')
    }
    req = requests.post(url = url, files = files)
    req.close()


def SendText(text:str, serverId):
    if len(text) == 0 :
        return 
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={Top10Alert}&text={text}&parse_mode=html&message_thread_id={tgThreadMapping[serverId]}&parse_mode=html"
    # url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={MY_Group}&text={text}&parseMode=html"
    req = requests.post(url = url)
    req.close()

if __name__ == "__main__" :
    pass
