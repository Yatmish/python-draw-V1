import cv2
import math
import numpy as np
from time import sleep
from scipy import spatial
from pynput.mouse import Controller, Button

mouse = Controller()

img_path = ''

im = cv2.imread(img_path, 2)

im90 = cv2.rotate(im, cv2.ROTATE_90_COUNTERCLOCKWISE)

flipVertical = cv2.flip(im90, 0)

ret, bw_img = cv2.threshold(flipVertical, 128, 255, cv2.THRESH_BINARY)

cv2.imwrite('savedFile.png', bw_img)

binaryImg = cv2.imread('./savedFile.png')

black = [0, 0, 0]

blackX, blackY = np.where(np.all(binaryImg == black, axis=2))

allBlackPoints = list(zip(blackX, blackY))

tree = spatial.KDTree(allBlackPoints)

firstX = allBlackPoints[0][0]
firstY = allBlackPoints[0][1]

del allBlackPoints[0]

print(len(allBlackPoints))

tree = spatial.KDTree(allBlackPoints)

sleep(5)

while allBlackPoints != []:
    try:
        allBlackPoints = list(filter(lambda x: isinstance(x, tuple), allBlackPoints))

        tree = spatial.KDTree(allBlackPoints)
        
        desireIndex = int(tree.query([(firstX, firstY)])[1])

        coordinates = allBlackPoints[desireIndex]

        mouse.position = (coordinates[0] + 5, coordinates[1] + 144)
        mouse.click(Button.left)

        firstX = allBlackPoints[desireIndex][0]
        firstY = allBlackPoints[desireIndex][1]

        allBlackPoints[desireIndex] = ''
    except:
        break
