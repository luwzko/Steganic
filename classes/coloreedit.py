from .utilities import *

try:
    from PIL import Image
except ImportError:
    print(f"{Fore.RED}[-] Install Pillow (PIL) using pip or pip3...{Fore.RESET}")

class ColorEdit:

    def __init__(self):
        self.input_img = ""
        self.output_img = "output.png"
        self.utils = Utils()

    def set_input_img(self, img):
        self.input_img = img

    def get_input_img(self):
        return self.input_img

    def set_output_img(self, img):
        self.output_img = img

    def get_output_img(self):
        return self.output_img

    def write(self, msg):
        try:
            im = Image.open(self.input_img).convert("RGB")
            width, height = im.size

            msg = self.utils.msg2bin(msg)
            im.putpixel((width - 1, height - 1), (0xCE, 0, len(msg)))

            x, y = 0, 0

            for c in [msg[i:i+8] for i in range(0, len(msg), 8)]:
                r, g, b = im.getpixel((x, y))
                r, g, b = self.utils.clr2bin(r), self.utils.clr2bin(g), self.utils.clr2bin(b)

                r = r[:-3] + c[:3]
                g = g[:-2] + c[3:5]
                b = b[:-3] + c[5:]

                r, g, b = int(r, 2), int(g, 2), int(b, 2)
                im.putpixel((x, y), (r, g, b))

                x += 1
                if x == width:
                    x = 0
                    y += 1

            print(f"{Fore.LIGHTYELLOW_EX}[.] Successfully wrote message in file {self.output_img}.{Fore.RESET}")
            im.save(self.output_img, "PNG")
            im.close()
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}[!] Exception occured: {e}.{Fore.RESET}")

    def read(self):
        try:
            im = Image.open(self.output_img).convert("RGB")
            width, height = im.size

            binary = ""
            msg_length = im.getpixel((width - 1, height - 1))[-1]

            for y in range(height):
                for x in range(width):
                    
                    r, g, b = im.getpixel((x, y))
                    r, g, b = self.utils.clr2bin(r), self.utils.clr2bin(g), self.utils.clr2bin(b)

                    binary += r[-3:] + g[-2:] + b[-3:]
                    msg_length -= 8

                    if msg_length == 0:
                        break
                break
            msg = self.utils.bin2msg(binary)

            print(f"{Fore.LIGHTYELLOW_EX}[.] Successfully decoded from {self.output_img} file.{Fore.RESET}")
            print(f"{Fore.LIGHTYELLOW_EX}[+]Message: {Fore.CYAN}{msg}{Fore.RESET}")
            im.close()
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}[!] Exception occurred: {e}.{Fore.RESET}")