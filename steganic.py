try:
    from colorama import Fore, init, Back
    pass
except ImportError:
    print("[-] Install Colorama using pip or pip3...")
from main_func.write_func import *
from main_func.read_func import *
from utils.write_util import *
from utils.read_util import *
from max_msg_length import *
import optparse
import os
try:    from PIL import *
except ImportError:
    print(f"{Fore.RED}[-] Install Pillow (PIL) using pip or pip3...{Fore.RESET}")

def banner():
    print(
        f"""
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
                                                                                                        {Fore.RESET}
        \t\t\t{Back.RED}{Fore.BLACK} }}-- Written by akxri --{{ {Back.RESET}{Fore.RESET}
        {Fore.LIGHTBLUE_EX}
        !> ;ByteEditing mode writes bits of message to B and G colors
        !> ;Coloredit mode writes color based on bits of message
        {Fore.CYAN}!> Steganic can only read messages written by Steganic.
                                                     {Fore.RESET}""")

def optparse_setup():
    parser = optparse.OptionParser(f"usage> {os.path.basename(__file__)} -m <mode> -f <file> --msg <message>")
    parser.add_option("-m", dest="mode", type="string", help="specify mode for Steganic program.")
    parser.add_option("-f", dest="file", type="string", default="steganic_output.png", help="specify file for Steganic program.")
    parser.add_option("--msg", dest="msg", type="string", default="SteganicDefault", help="specify message to write for Steganic program.")
    (options, args) = parser.parse_args()
    if (options.mode == None):
        print(parser.usage)
        exit(0)
    else:

        script_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_path)

        mode = options.mode
        file = options.file
        msg = options.msg

        return mode, file, msg

def steganic(mode, file, msg):
    if mode == "Write;Coloredit":
        banner()
        print(f"{Fore.LIGHTYELLOW_EX}[+] Checking Size of message...{Fore.RESET}")
        print(f"{Fore.LIGHTYELLOW_EX}[+] Done... Good")
        max_msg_len = get_maximum_msg_length(file)

        if len(msg) <= max_msg_len:

            file_to_continue = pxwritelength(file, msg)
            output_string = message_to_bytearray(msg)
            write_coloredit(file_to_continue, output_string, msg)

        elif len(msg) >= max_msg_len:

            print(f"{Fore.LIGHTRED_EX} Error, too big message.{Fore.RESET}")
            exit(0)

    elif mode == "Write;ByteEditing":
        banner()
        print(f"{Fore.LIGHTYELLOW_EX}[+] Checking Size of message...{Fore.RESET}")
        print(f"{Fore.LIGHTYELLOW_EX}[+] Done... Good")
        max_msg_len = get_maximum_msg_length(file)

        if len(msg) <= (max_msg_len * 2):

            file_to_continue = pxwritelength(file, msg)
            output_string = message_to_bytearray(msg)
            write_byteediting(file_to_continue, output_string, msg)

        elif len(msg) >= max_msg_len:

            print(f"{Fore.LIGHTRED_EX} Error, too big message.{Fore.RESET}")
            exit(0)

    elif mode == "Read;ByteEditing":
        banner()
        print(f"{Fore.LIGHTYELLOW_EX}[+] Decoding...{Fore.RESET}")
        msg_length = pxreadlength(file)
        read_byteediting(msg_length, file)


    elif mode == "Read;Coloredit":
        banner()
        print(f"{Fore.LIGHTYELLOW_EX}[+] Decoding...{Fore.RESET}")

        msg_length = coloredit_pxreadlength(file)
        read_coloredit(msg_length, file)

    else:
        print(f"""{Fore.LIGHTRED_EX}
 <#@ ERROR @#>
[!]Please choose a mode:
  (1.)Write;Coloredit
  (2.)Read;Coloredit
  (3.)Write;ByteEditing
  (4.)Read;ByteEditing{Fore.RESET}""")
        exit()

init()
setup_args = optparse_setup()
steganic(setup_args[0], setup_args[1], setup_args[2])
