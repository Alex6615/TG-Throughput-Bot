import os 
import time
from datetime import datetime
import multiprocessing as mp
import random

import logging
import requests
import asyncio
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, ApplicationBuilder, ContextTypes, CommandHandler


try :
    from secret_account import allow_groups
    from secret_telegram import TELEGRAM_TOKEN
except :
    from secrets.secret_account import allow_groups
    from secrets.secret_telegram import TELEGRAM_TOKEN
#from secret_telegram_local import TELEGRAM_TOKEN
#from secret_account_local import allow_groups
from driver_execute import imageGetter
from image_resize import image_Crop
from time_generator import ts_generator
from telegram_sender import SendPhoto, SendText
from oclock import isoclock, minuteisfive, minuteisten
from query_tools import UserGetter



t_token = TELEGRAM_TOKEN
loop_status = True

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.id not in allow_groups :
        print(f"Group {update.message.chat.id} not allow !")
        return
    await context.bot.send_message(chat_id=update.effective_chat.id, text="📘 I'm a throughput Bot")

'''
async def throughput(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #print(update.message)
    if update.message.chat.id not in allow_groups :
        print(f"Group {update.message.chat.id} not allow !")
        return
    print("generating timestamps ....")
    ts_now, ts_before = ts_generator(range=10)
    print("downloading image ....")
    img_name = get_Image(ts_now, ts_before)
    if img_name == None :
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Image Download Faliure !")
    else :
        print("resizing image ....")
        image_Crop(img_name)
        print("Image resized complete !")
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=f"./resized_png/r-{img_name}")

async def count(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.id not in allow_groups :
        print(f"Group {update.message.chat.id} not allow !")
        return
    x = Get_Wking_UserCount()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=x)
'''

def Activate_bot():
    # pwd
    pwd = os.getcwd()
    if not os.path.exists(f"{pwd}/png"):
        os.mkdir(f"{pwd}/png")
    if not os.path.exists(f"{pwd}/resized_png"):
        os.mkdir(f"{pwd}/resized_png")    
    start_handler = CommandHandler('start', start)
    application = ApplicationBuilder().token(t_token).build()
    application.add_handler(start_handler)
    application.run_polling(timeout=10, poll_interval=5)

def throughput_loop(): 
    serverIds = [
        9, # wking 
        103, #dobet
    ]
    while(loop_status):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        isten = minuteisten()
        print(f"[{current_time}] Is oclock ?  {isten}")
        if isten == False :
            time.sleep(45)
            continue
        try :
            ts_now, ts_before = ts_generator(range=10)
            imgGetter = imageGetter()
            for server in serverIds :
                # online user count
                user = UserGetter(serverId=server)
                usercount = user.Get_UserCount()
                # online throughput image
                imgGetter.grafanaLogin()
                img_result = imgGetter.getImage(ts_now, ts_before, serverId=server)
                if img_result == 0 :
                    SendText(text=usercount + "\n<b>img download failed</b>", serverId=server)
                else :
                    resized_image = image_Crop(img_result)
                    SendPhoto(resized_image, serverId=server, text=usercount)
            imgGetter.quitdriver()
        except Exception as e:
            print(e)
        time.sleep(60)

def main():
    process_lists = []
    print("bot added")
    process_lists.append(mp.Process(target=Activate_bot))
    process_lists[0].start()
    print("loop added")
    process_lists.append(mp.Process(target=throughput_loop))
    process_lists[1].start()
    for process in process_lists :
        process.join()

if __name__ == '__main__':
    main()
