from PIL import Image

def pxwritelength(image_file, msg):
    try:
        im = Image.open(image_file)
        rgb = im.convert("RGB")
        width, height = im.size
        pixel_tuple = rgb.getpixel((width - 1, height - 1))
        rgb.putpixel((width - 1, height - 1), (pixel_tuple[0], pixel_tuple[1], 125 - len(msg)))
        rgb.save("steganic_temp_deleteafter.png", "PNG")
        im.close()
        return "steganic_temp_deleteafter.png"
    except Exception as e:
        input("Error, Press enter to quit the program...")
        print(e)

def message_to_bytearray(msg):
    output_string = ""
    try:
        for char in msg:
            ord_char = ord(char)
            bin_char_changed = "0" * (8 - len(bin(ord_char)[2:])) + bin(ord_char)[2:]
            output_string += bin_char_changed
        return output_string
    except:
        print("Error")
