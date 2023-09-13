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

from secret_telegram_local import TELEGRAM_TOKEN
from driver_execute import get_Image
from image_resize import image_Crop
from time_generator import ts_generator
from telegram_sender import SendPhoto, SendText
from oclock import isoclock, minuteisfive
from query_tools import Get_Wking_UserCount


t_token = TELEGRAM_TOKEN
loop_status = True
allow_groups = [
    -1001507912886,
    -1001935582944,
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.id not in allow_groups :
        print(f"Group {update.message.chat.id} not allow !")
        return
    await context.bot.send_message(chat_id=update.effective_chat.id, text="📘 I'm a throughput Bot")

async def throughput(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.id not in allow_groups :
        print(f"Group {update.message.chat.id} not allow !")
        return
    print("generating timestamps ....")
    ts_now, ts_before = ts_generator()
    print("downloading image ....")
    img_name = get_Image(ts_now, ts_before)
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

def Activate_bot():
    # pwd
    pwd = os.getcwd()
    if not os.path.exists(f"{pwd}/png"):
        os.mkdir(f"{pwd}/png")
    if not os.path.exists(f"{pwd}/resized_png"):
        os.mkdir(f"{pwd}/resized_png")  
    print("Hasaki 吹起來")   
    start_handler = CommandHandler('start', start)
    count_handler = CommandHandler('count', count)
    throughput_handler = CommandHandler('throughput', throughput)
    application = ApplicationBuilder().token(t_token).build()
    application.add_handler(start_handler)
    application.add_handler(throughput_handler)
    application.add_handler(count_handler)
    application.run_polling()

def throughput_loop(): 
    #session = requests.session()
    while(loop_status):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        # print(f"looping {random.randrange(1,100,2)}")
        isfive = minuteisfive()
        print(f"[{current_time}] Is oclock ?  {isfive}")
        if isfive == False :
            time.sleep(30)
            continue
        try :
            ts_now, ts_before = ts_generator()
            img_name = get_Image(ts_now, ts_before)
            resized_image = image_Crop(img_name)
        except :
            continue
        usercount = Get_Wking_UserCount()
        reply = '🌏 Wking Online Users Now : ' + usercount
        SendText(reply)
        print("Sending photo .....")
        SendPhoto(resized_image)
        print("Send photo complete !")
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