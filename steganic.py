from classes import byteedit, coloreedit, utilities, settings
from colorama import Fore, init, Back

class Steganic:
    def __init__(self):
        self.color_editor = coloreedit.ColorEdit()
        self.byte_editor = byteedit.ByteEdit()

        self.settings_manager = settings.Settings()
        self.utils = utilities.Utils()
        
    def main(self):
        init()
        self.utils.print_banner()

        cmd = ""

        while (cmd not in ["quit", "exit"]):
            
            print(self.utils.console, end=" "); cmd = str(input())
            arguments = cmd.split(" ")
            
            match arguments[0]:
                case "set":
                    match arguments[1]:
                        case "input_img":  self.settings_manager.set_input_img(arguments[2])
                        case "output_img": self.settings_manager.set_output_img(arguments[2])
                        case "mode":       self.settings_manager.set_mode(arguments[2])
                        case "msg":        self.settings_manager.set_msg(arguments[2])
                case "list":
                    self.utils.list_setts(self.settings_manager)
                case "detect":
                    self.utils.detect(arguments[1])
                case "run":
                    if self.settings_manager.all_set():
                        match self.settings_manager.get_mode():
                            case "ColorEdit":
                                self.color_editor.set_input_img(self.settings_manager.get_input_img())
                                self.color_editor.set_output_img(self.settings_manager.get_output_img())
                                match arguments[1]:
                                    case "Write":
                                        self.color_editor.write(self.settings_manager.get_msg())
                                    case "Read":
                                        self.color_editor.read()

                            case "ByteEdit":
                                self.byte_editor.set_input_img(self.settings_manager.get_input_img())
                                self.byte_editor.set_output_img(self.settings_manager.get_output_img())
                                match arguments[1]:
                                    case "Write":
                                        self.byte_editor.write(self.settings_manager.get_msg())
                                    case "Read":
                                        self.byte_editor.read()
                
                case "help":
                    self.utils.print_help()
        exit()
if __name__ == "__main__":
    steganic = Steganic()
    steganic.main()
