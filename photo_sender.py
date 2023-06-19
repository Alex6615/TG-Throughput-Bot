import requests
import os



def SendPhoto(photo_name):
    if len(photo_name) == 0 :
        return 
    # my test group
    # chat_id = "-955174563"
    # mis_alert chat-id
    mis_alert = "-1001507912886"
    url = f"https://api.telegram.org/bot5780018337:AAG8qusjqd1xYrPG4iI3yrJm1dHvyRZjlU8/sendPhoto?chat_id={mis_alert}"
    pwd = os.getcwd()
    file = f"{pwd}/resized_png/{photo_name}"
    files = {
        'photo': open(file, 'rb')
    }
    req = requests.post(url = url, files = files)
    req.close()

if __name__ == "__main__" :
    pass