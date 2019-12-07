from PIL import Image
import math

def calculate_diagonal(x,y):
    x_squared = (x ** 2)
    y_squared = (y ** 2)
    combined = x_squared + y_squared
    return round(math.sqrt(combined), 0) - 2

def get_maximum_msg_length(file):
    im = Image.open(file)
    width, height = im.size
    result = calculate_diagonal(width, height)
    im.close()
    return int(result)
