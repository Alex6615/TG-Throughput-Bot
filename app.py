import os 
import time
import multiprocessing as mp
import random

import logging
import requests
import asyncio
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, ApplicationBuilder, ContextTypes, CommandHandler

from secret_telegram import TELEGRAM_TOKEN
from driver_execute import get_Image
from image_resize import image_Crop
from time_generator import ts_generator



t_token = TELEGRAM_TOKEN
loop_status = True
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="📘 I'm a throughput Bot")

async def throughput(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("generating timestamps ....")
    ts_now, ts_before = ts_generator()
    print("downloading image ....")
    img_name = get_Image(ts_now, ts_before)
    print("resizing image ....")
    image_Crop(img_name)
    print("Image resized complete !")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=f"./resized_png/r-{img_name}")

def Activate_bot():
    if not os.path.exists("png"):
        os.mkdir("png")
    if not os.path.exists("resized_png"):
        os.mkdir("resized_png")  
    print("hasaki")   
    start_handler = CommandHandler('start', start)
    throughput_handler = CommandHandler('throughput', throughput)
    application = ApplicationBuilder().token(t_token).build()
    application.add_handler(start_handler)
    application.add_handler(throughput_handler)
    application.run_polling()

def throughput_loop(): 
    #session = requests.session()
    while(loop_status):
        #ts_now, ts_before = ts_generator()
        #img_name = get_Image(ts_now, ts_before)
        #image_Crop(img_name)
        print(f"looping {random.randrange(1,100,2)}")
        time.sleep(1)

def main():
    process_lists = []
    process_lists.append(mp.Process(target=Activate_bot))
    process_lists[0].start()
    process_lists.append(mp.Process(target=throughput_loop))
    process_lists[1].start()

    for process in process_lists :
        process.join()



if __name__ == '__main__':
    main()
    #Activate_bot()