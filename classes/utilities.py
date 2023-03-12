try:
    from colorama import Fore, init, Back
except ImportError:
    print("[-] Install Colorama using pip or pip3...")
try:
    from PIL import Image
except ImportError:
    print(
        f"{Fore.RED}[-] Install Pillow (PIL) using pip or pip3...{Fore.RESET}")


class Utils:
    def __init__(self):
        self.banner = f"""
            {Fore.LIGHTGREEN_EX}
     @@@@@@   @@@@@@@  @@@@@@@@   @@@@@@@@   @@@@@@   @@@  @@@  @@@   @@@@@@@
    @@@@@@@   @@@@@@@  @@@@@@@@  @@@@@@@@@  @@@@@@@@  @@@@ @@@  @@@  @@@@@@@@
    !@@         @@!    @@!       !@@        @@!  @@@  @@!@!@@@  @@!  !@@
    !@!         !@!    !@!       !@!        !@!  @!@  !@!!@!@!  !@!  !@!
    !!@@!!      @!!    @!!!:!    !@! @!@!@  @!@!@!@!  @!@ !!@!  !!@  !@!
     !!@!!!     !!!    !!!!!:    !!! !!@!!  !!!@!!!!  !@!  !!!  !!!  !!!
         !:!    !!:    !!:       :!!   !!:  !!:  !!!  !!:  !!!  !!:  :!!
        !:!     :!:    :!:       :!:   !::  :!:  !:!  :!:  !:!  :!:  :!:
    :::: ::      ::     :: ::::   ::: ::::  ::   :::   ::   ::   ::   ::: :::
    :: : :       :     : :: ::    :: :: :    :   : :  ::    :   :     :: :: :
    {Fore.RESET}\t\t\t   -- {Fore.LIGHTBLACK_EX}Written by luwzko{Fore.LIGHTBLACK_EX} --
    {Fore.LIGHTBLUE_EX}
    !> ByteEditing mode writes bits of message to B and G colors
    !> ColorEdit mode writes color based on bits of message
    {Fore.CYAN}!> {Fore.GREEN}Steganic{Fore.CYAN} can only read messages written by {Fore.GREEN}Steganic{Fore.CYAN}.{Fore.RESET}\n"""
        
        self.help = f"""{Fore.LIGHTGREEN_EX}
    Steganic Commands Info:
        {Fore.CYAN}[+]{Fore.LIGHTBLUE_EX} set - set setting values for running Steganic
                input_img  - path of the image for operations
                output_img - path for the image that will be saved and created in that file location.
                msg        - msg that needs to be written
                mode       - selectable mode for Steganic       
        {Fore.CYAN}[+]{Fore.LIGHTBLUE_EX} detect - detect if a image was edited by Steganic and if yes returns which mode
        {Fore.CYAN}[+]{Fore.LIGHTBLUE_EX} list   - lists all settings
        {Fore.CYAN}[+]{Fore.LIGHTBLUE_EX} help   - displays this help message.
        {Fore.CYAN}[+]{Fore.LIGHTBLUE_EX} run    - run currently selected mode with selected values
    [!] Possible modes are ColorEdit and ByteEdit with operation Read/Write
    {Fore.LIGHTGREEN_EX}
    Steganic Commands Syntax:
        {Fore.CYAN}[+]{Fore.LIGHTBLUE_EX} set input_img|output_img|mode|msg value
        {Fore.CYAN}[+]{Fore.LIGHTBLUE_EX} detect img_path
        {Fore.CYAN}[+]{Fore.LIGHTBLUE_EX} list
        {Fore.CYAN}[+]{Fore.LIGHTBLUE_EX} help
        {Fore.CYAN}[+]{Fore.LIGHTBLUE_EX} run
    {Fore.RESET}"""
        self.console = f"{Back.LIGHTCYAN_EX}steganic{Back.LIGHTBLUE_EX}>{Back.RESET} "

    def print_banner(self):
        print(self.banner)
        
    def print_help(self):
        print(self.help)

    def msg2bin(self, msg):
        return ('0' + '0'.join(format(ord(x), 'b') for x in msg))

    def bin2msg(self, bin_str):
        return (''.join(chr(int(bin_str[i:i+8], 2)) for i in range(0, len(bin_str), 8)))

    def clr2bin(self, clr):
        return format(clr, "08b")

    # utility command functions
    def list_setts(self, settings_manager): # list commands
        sett_list = settings_manager.get_settings_list()
        print(f"{Fore.LIGHTGREEN_EX}[I]{Fore.LIGHTBLUE_EX} Running list command...")
        for sett in sett_list:
            print(f"\t{Fore.LIGHTBLUE_EX}[+]{Fore.LIGHTCYAN_EX} {sett} - {sett_list[sett]}{Fore.RESET}")

    def detect(self, path): # detect command
        try:
            im = Image.open(path).convert("RGB")
            width, height = im.size
            mode = im.getpixel((width - 1, height - 1))[0]
            print(f"{Fore.LIGHTGREEN_EX}[O]{Fore.LIGHTBLUE_EX} Running Detect command on {Fore.YELLOW}{path}")
            if mode == 0xCE:
                print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTBLUE_EX} Detected mode is {Fore.LIGHTGREEN_EX}ColorEdit.{Fore.RESET}")
            elif mode == 0xBE:
                print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTBLUE_EX} Detected mode is {Fore.LIGHTGREEN_EX}ByteEdit.{Fore.RESET}")
            else:
                print(f"{Fore.RED}[:/]{Fore.LIGHTBLUE_EX} No mode was detected.{Fore.RESET}")
            im.close()
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}[!] Exception occured: {e}.{Fore.RESET}")
