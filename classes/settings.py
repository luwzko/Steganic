class Settings:
    def __init__(self):
        self.input_img = ""
        self.output_img = ""
        self.mode = ""
        self.msg = ""

    def set_input_img(self, input_img):
        self.input_img = input_img

    def get_input_img(self):
        return self.input_img

    def set_output_img(self, output_img):
        self.output_img = output_img

    def get_output_img(self):
        return self.output_img

    def set_mode(self, mode):
        self.mode = mode

    def get_mode(self):
        return self.mode

    def set_msg(self, msg):
        self.msg = msg

    def get_msg(self):
        return self.msg

    def get_settings_list(self):
        return {"input_img":self.input_img, "output_img":self.output_img, "mode":self.mode, "msg":self.msg}
        
    def all_set(self):
        return (self.input_img and self.output_img and self.mode and self.msg)