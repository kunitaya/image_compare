# -*- coding: utf-8 -*-
from skimage.measure import compare_ssim
import imutils
import cv2
import os
import sys

# Logging
from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

header_A = 'after'
header_B = 'before'
header_C = 'compare'

def find_all_files(directory = os.path.abspath(__file__)):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

def compare_image(str_path):
    fileA = os.path.join(os.path.dirname(os.path.abspath(__file__)), header_A, str_path)
    fileB = os.path.join(os.path.dirname(os.path.abspath(__file__)), header_B, str_path)
    pathC = os.path.dirname(os.path.join(os.path.dirname(os.path.abspath(__file__)), header_C, str_path))

    if not os.path.exists(pathC): os.makedirs(pathC)

    imageA = cv2.imread(fileA, 1)
    imageB = cv2.imread(fileB, 1)
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    try:
        (score, diff) = compare_ssim(grayA, grayB, full=True, multichannel=True)
        diff = (diff * 255).astype("uint8")

    except ValueError as e:
        logger.debug(str_path + ": ZeroDivisionError")
        return 0
    except:
        logger.debug(str_path + ": " + "Unexpected error: ", sys.exc_info()[0])
        return 0

    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]

    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

    if score < 0:
        percent = ((score * 100) / 2) - 50
        logger.debug(fileA + ', ' + fileB + ', ' + "Similarity: {0}%".format(percent))

    else:
        percent = round(((score * 100) / 2) + 50, 2)
        logger.debug(fileA + ', ' + fileB + ', ' + "Similarity: {0}%".format(percent))

    cv2.imwrite(os.path.join(pathC, header_A + '.png'), imageA)
    cv2.imwrite(os.path.join(pathC, header_B + '.png'), imageB)
    cv2.waitKey(0)

absdir = os.path.dirname(os.path.abspath(__file__))
filesA = filter(lambda f:os.path.isfile(f), find_all_files(os.path.join(absdir, header_A)))
mapA = map(lambda s:s.replace(os.path.join(absdir, header_A) + os.sep, ''),filesA)
filesB = filter(lambda f:os.path.isfile(f), find_all_files(os.path.join(absdir, header_B)))
mapB = map(lambda s:s.replace(os.path.join(absdir, header_B) + os.sep, ''),filesB)

path = list(set(mapA) & set(mapB))

if __name__ == '__main__':
    list(map(compare_image, path))
    print("Process Done")
