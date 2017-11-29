from skimage.measure import compare_ssim
import imutils
import cv2
import os

header_A = 'after'
header_B = 'before'
header_out = 'compare'

def find_all_files(directory = os.path.abspath(__file__)):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

def compare_image():
    text_file = open(os.path.join(header_out, 'output.syslog'), 'a')
    for i in range(len(path)):
        fileA = os.path.join(os.path.dirname(os.path.abspath(__file__)), header_A, path[i])
        fileB = os.path.join(os.path.dirname(os.path.abspath(__file__)), header_B, path[i])
        imageA = cv2.imread(fileA, 0)
        imageB = cv2.imread(fileB, 0)

        #grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        #grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

        #(score, diff) = compare_ssim(grayA, grayB, full=True, multichannel=True)
        try:
            (score, diff) = compare_ssim(imageA, imageB, full=True, multichannel=True)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            continue

        diff = (diff * 255).astype("uint8")

        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]

        for c in cnts:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

        if score < 0:
            percent = ((score * 100) / 2) - 50
        else:
            percent = round(((score * 100) / 2) + 50, 2)
            fie = os.path.join(header_A + path[i] + '\\a.png\n', header_B + path[i] + '\\a.png\n')
            text_file.write(header_A + path[i] + '\\a.png, '
                            + header_B + path[i] + '\\a.png, '
                            + "Similarity: %s" % percent + """%""" + "\n")

        cv2.imwrite(os.path.join(os.path.join(header_out + path[i]), 'check-result-20171005233158.png'), imageA)
        cv2.imwrite(os.path.join(os.path.join(header_out + path[i]), 'check-result-20171016144416.png'), imageB)
        cv2.waitKey(0)
        print(path[i])
    text_file.close()

absdir = os.path.dirname(os.path.abspath(__file__))
filesA = filter(lambda f:os.path.isfile(f), find_all_files(os.path.join(absdir, header_A)))
mapA = map(lambda s:s.replace(os.path.join(absdir, header_A), ''),filesA)
filesB = filter(lambda f:os.path.isfile(f), find_all_files(os.path.join(absdir, header_B))):
mapB = map(lambda s:s.replace(os.path.join(absdir, header_B), ''),filesB)

path = list(set(list(mapA)) & set(list(mapB)))

compare_image()
print("Process Done")
