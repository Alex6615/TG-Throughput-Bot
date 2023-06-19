import os 

from PIL import Image


def image_Crop(img_name):
    pwd = os.getcwd()
    img = Image.open(f"{pwd}/png/{img_name}")
    print(f"Original image size : {img.size}")
    box = (0, 100, 800, 500)
    resized = img.crop(box)
    resized.save(f"{pwd}/resized_png/r-{img_name}")
    print("Resize Complete !")
    return f"r-{img_name}"


if __name__ == "__main__" :
    pass