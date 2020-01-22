from PIL import Image
from colorama import Fore, init, Back

def pxreadlength(image_file):
    try:
        im = Image.open(image_file)
        rgb = im.convert("RGB")
        width, height = im.size
        rgb_tuple = rgb.getpixel((width - 1, height - 1))
        x = abs(125 - rgb_tuple[-1])
        im.close()
        return x * 4
    except FileNotFoundError as e:
        pass
    except Exception as e:
        input("Error, Press enter to quit the program...")
        print(e)

def coloredit_pxreadlength(image_file):
    try:
        im = Image.open(image_file)
        rgb = im.convert("RGB")
        width, height = im.size
        rgb_tuple = rgb.getpixel((width - 1, height - 1))
        x = abs(125 - rgb_tuple[-1])
        im.close()
        return x * 8
    except FileNotFoundError as e:
        pass
    except Exception as e:
        input("Error, Press enter to quit the program...")
        print(e)
