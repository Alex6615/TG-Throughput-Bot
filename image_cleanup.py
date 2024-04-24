import os
from datetime import datetime, timedelta


def cleanup(path):
    # all images in dir png
    files = os.listdir(path)    
    for file in files :
        file_timestamp = file.split('-')[-1].split('.')[0][:-3]
        file_datetime = datetime.fromtimestamp(int(file_timestamp))
        datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("file : ", end = " ")
        print(file_datetime)
        print("now : ", end = " ")
        print(datetime_now)
        # 時間差
        range = datetime.now() - file_datetime
        print(range.days)
        # 超過一天就移除
        if range.days > 0 :
            print(f"delete file {file}")
            os.remove(f"{path}/{file}")
        else :
            print(f"{file} no need to be deleted")
        print("----------")

if __name__ == "__main__" :
    pwd = os.getcwd()
    cleanup(f"{pwd}/png")
    cleanup(f"{pwd}/resized_png")
