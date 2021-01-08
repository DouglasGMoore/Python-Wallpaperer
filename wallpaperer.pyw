# from PIL import Image
import os
import random
import ctypes

arr = os.listdir("C:/Users/showe/OneDrive/Pictures/wallpaper")
pick_name_from_list = []
for i in arr:
    pick_name_from_list.append(i)

pick = random.choice(pick_name_from_list)

image = f'C:/Users/showe/OneDrive/Pictures/wallpaper/{pick}'
imagePath = image


def changeBG(imagePath):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imagePath , 0)
    return;

changeBG(imagePath)
