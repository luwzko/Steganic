from colorama import Fore
from PIL import Image

def write_byteediting(image_file, output_string, msg):
    try:

        im = Image.open(image_file)
        width, height = im.size
        rgb = im.convert("RGB")

        write_x = 0
        write_y = 0

        iter_byte = iter(output_string)
        print(output_string, len(output_string))
        for bits in iter_byte:

            current_color = rgb.getpixel((write_x, write_y))

            changed_green = list(bin(current_color[1])[2:])
            changed_green[-1] = bits
            joined_green = "".join(changed_green)

            changed_blue = list(bin(current_color[2])[2:])
            changed_blue[-1] = next(iter_byte)
            joined_blue = "".join(changed_blue)

            new_color = (current_color[0], int(joined_green, 2), int(joined_blue,2))
            rgb.putpixel((write_x, write_y), new_color)
            write_x += 1
            write_y += 1

            if write_x >= width:

                write_x = 0
                write_y += 1

            if write_y >= height:

                write_y = 0
                write_x += 1

        print(f"{Fore.LIGHTYELLOW_EX}[.] Successfully wrote {msg}.{Fore.RESET}")
        rgb.save("steganic_output.png", "PNG")
        im.close()
    except Exception as e:
        input("Error, Press enter to quit the program...")
        print(e)

def write_coloredit(file, output_string, msg):
    try:

        im = Image.open(file)
        width, height = im.size
        rgb = im.convert("RGB")

        write_x = 0
        write_y = 0

        for bit in output_string:

            current_color = rgb.getpixel((write_x, write_y))
            if bit == "0":

                new_color = (current_color[0], current_color[1], 254)
                rgb.putpixel((write_x, write_y), new_color)
                write_x += 1
                write_y += 1

            elif bit == "1":

                new_color = (current_color[0], current_color[1], 255)
                rgb.putpixel((write_x, write_y), new_color)
                write_x += 1
                write_y += 1
            if write_x >= width:

                write_x = 0
                write_y += 1

            if write_y >= height:

                write_y = 0
                write_x += 1

        print(f"{Fore.LIGHTYELLOW_EX}[.] Successfully wrote {msg}.{Fore.RESET}")
        rgb.save("steganic_output.png", "PNG")
        im.close()
    except Exception as e:
        input("Error, Press enter to quit the program...")
        print(e)
