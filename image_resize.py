import os 

from PIL import Image


def image_Crop(img_name):
    pwd = os.getcwd()
    img = Image.open(f"{pwd}/png/{img_name}")
    print(f"Original image size : {img.size}")
    # box=(left,top,right,bottom)
    box = (450, 250, 1450, 780)
    resized = img.crop(box)
    resized.save(f"{pwd}/resized_png/r-{img_name}")
    print("Resize Complete !")
    return f"r-{img_name}"


if __name__ == "__main__" :
    x = image_Crop('throughput-1695005706000.png')
    print(x)