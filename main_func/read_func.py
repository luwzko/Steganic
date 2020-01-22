from colorama import Fore
from PIL import Image

def read_coloredit(msg_length, file):
    try:

        im = Image.open(file)
        binary_str = ""

        for x in range(0, msg_length):
            rgb_tuple = im.getpixel((x,x))

            if rgb_tuple[-1] == 254:
                binary_str += "0"

            elif rgb_tuple[-1] == 255:
                binary_str += "1"

        print(f"{Fore.LIGHTYELLOW_EX}[+]Message:{Fore.CYAN} ", end="")
        for chrs in range(0, len(binary_str)+1, 8):
            try:
                bin_string = binary_str[chrs : chrs + 8]
                chr_string = chr(int(bin_string, 2))
                print(chr_string, end="")
            except ValueError:
                pass
        print(f"{Fore.RESET}")
        print(f"{Fore.LIGHTYELLOW_EX}[.] Successfully decoded.{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}Error : unknown file {Fore.RESET}")

def read_byteediting(msg_length, file):
    try:
        im = Image.open(file)

        binary_str = ""

        for x in range(0, msg_length):
            rgb_tuple = im.getpixel((x, x))

            g = bin(rgb_tuple[1])[2:][-1]
            b = bin(rgb_tuple[2])[2:][-1]

            binary_str += g
            binary_str += b

        print(f"{Fore.LIGHTYELLOW_EX}[+]Message:{Fore.CYAN} ", end="")
        for chrs in range(0, len(binary_str), 8):
            try:
                bin_string = binary_str[chrs : chrs + 8]
                chr_string = chr(int(bin_string, 2))
                print(chr_string, end="")
            except ValueError:
                pass
        print(f"{Fore.RESET}")
        print(f"{Fore.LIGHTYELLOW_EX}[.] Successfully decoded.{Fore.RESET}")
    except FileNotFoundError as e:
        print(f"{Fore.LIGHTRED_EX}Error : unknown file {Fore.RESET}")
