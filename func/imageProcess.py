import cv2
import numpy as np


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
