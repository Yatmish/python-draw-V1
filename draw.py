import cv2
import numpy as np
from time import sleep
from pynput.mouse import Controller, Button

mouse = Controller()
CONSTANT = 0.000000000000000000000000000000000000000000000000000000000000000000000005

img_path = './img/test.png'
saved_path = './img/savedFile.png'


def getImage(img_path, saved):
    im = cv2.imread(img_path, 2)

    im90 = cv2.rotate(im, cv2.ROTATE_90_COUNTERCLOCKWISE)

    flipVertical = cv2.flip(im90, 0)

    ret, bw_img = cv2.threshold(flipVertical, 128, 255, cv2.THRESH_BINARY)

    cv2.imwrite(saved, bw_img)


def toBinary(saved_path):
    binaryImg = cv2.imread('./savedFile.png')

    black = [0, 0, 0]

    blackX, blackY = np.where(np.all(binaryImg == black, axis=2))

    return list(zip(blackX, blackY))


def get_ordered(points):
    points.sort(key=lambda p: (p[0] - 0.0) ** 2 + (p[1] - 0.0)**2)
    return points


getImage(img_path=img_path, saved=saved_path)

allBlackPoints = toBinary(saved_path=saved_path)

sleep(5)

for coordinate in get_ordered(allBlackPoints):
    sleep(CONSTANT)
    mouse.position = (coordinate[0] + 5, coordinate[1] + 144)
    mouse.click(Button.left)
