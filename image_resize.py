import os 

from PIL import Image


def image_Crop(img_name):
    pwd = os.getcwd()
    img = Image.open(f"{pwd}/png/{img_name}")
    print(f"Original image size : {img.size}")
    # box=(left,top,right,bottom)
    width = img.size[0]
    length = img.size[1]
    #box = (width*0.23, length*0.21, width*0.78, length*0.78)
    box = (width*0, length*0.15, width, length*0.935)
    resized = img.crop(box)
    resized.save(f"{pwd}/resized_png/r-{img_name}")
    print("Resize Complete !")
    return f"r-{img_name}"


if __name__ == "__main__" :
    x = image_Crop('throughput-1705369668000-103.png')
    print(x)