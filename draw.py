from drawingPython.functions.imageProcess import getImage, toBinary
from drawingPython.functions.mathFunc import get_ordered
from time import sleep
from pynput.mouse import Controller, Button

mouse = Controller()
CONSTANT = 0.000000000000000000000000000000000000000000000000000000000000000000000005

img_path = './img/test.png'
saved_path = './img/savedFile.png'

getImage(img_path=img_path, saved=saved_path)

allBlackPoints = toBinary(saved_path=saved_path)

sleep(5)

for coordinate in get_ordered(allBlackPoints):
    sleep(CONSTANT)
    mouse.position = (coordinate[0] + 5, coordinate[1] + 144)
    mouse.click(Button.left)
