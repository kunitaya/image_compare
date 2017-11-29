from skimage.measure import compare_ssim
import imutils
import cv2
import os

header_A = 'check-result-20171005233158'
header_B = 'check-result-20171016144416'
header_out = 'output'

path = [
    '\images\https_www.subaru.jp\\about\gallery',
    '\images\https_www.subaru.jp\\accessory\\brz',
    '\images\https_www.subaru.jp\\accessory\car_select',
    '\images\https_www.subaru.jp\\accessory\catalog',
    '\images\https_www.subaru.jp\\accessory\chiffon',
    '\images\https_www.subaru.jp\\accessory\engine_oil',
    '\images\https_www.subaru.jp\\accessory\exiga',
    '\images\https_www.subaru.jp\\accessory\\forester',
    '\images\https_www.subaru.jp\\accessory\impreza',
    '\images\https_www.subaru.jp\\accessory\justy',
    '\images\https_www.subaru.jp\\accessory\legacy',
    '\images\https_www.subaru.jp\\accessory\levorg',
    '\images\https_www.subaru.jp\\accessory\\navi_audio',
    '\images\https_www.subaru.jp\\accessory\\navi_audio\option',
    '\images\https_www.subaru.jp\\accessory\pleoplus',
    '\images\https_www.subaru.jp\\accessory\stella',
    '\images\https_www.subaru.jp\\accessory\\update',
    '\images\https_www.subaru.jp\\accessory\\versionup',
    '\images\https_www.subaru.jp\\accessory\wrxs4',
    '\images\https_www.subaru.jp\\accessory\wrxsti',
    '\images\https_www.subaru.jp\\accessory\\xv',
    '\images\https_www.subaru.jp\\accessory',
    '\images\https_www.subaru.jp\\afterservice\carcare',
    '\images\https_www.subaru.jp\\afterservice\cddb',
    '\images\https_www.subaru.jp\\afterservice\check',
    '\images\https_www.subaru.jp\\afterservice\dealer',
    '\images\https_www.subaru.jp\\afterservice\inspection',
    '\images\https_www.subaru.jp\\afterservice\maintenance',
    '\images\https_www.subaru.jp\\afterservice\\tnst',
    '\images\https_www.subaru.jp\\afterservice\warranty',
    '\images\https_www.subaru.jp\\afterservice',
    '\images\https_www.subaru.jp\\appli',
    '\images\https_www.subaru.jp\\appli\mysubaru',
    '\images\https_www.subaru.jp\\assist',
    '\images\https_www.subaru.jp\\brand\\technology\\technology',
    '\images\https_www.subaru.jp\\brz\\brz',
    '\images\https_www.subaru.jp\\brz\\brz\\top\system',
    '\images\https_www.subaru.jp\campaign',
    '\images\https_www.subaru.jp\campaign\shijo',
    '\images\https_www.subaru.jp\campaign\shijo\event\kosoku',
    '\images\https_www.subaru.jp\campaign\\topics\\anshinprotect3',
    '\images\https_www.subaru.jp\campaign\\topics\legacy_aero',
    '\images\https_www.subaru.jp\campaign\\topics\\xv_aero',
    '\images\https_www.subaru.jp\campaign',
    '\images\https_www.subaru.jp\carlineup',
    '\images\https_www.subaru.jp\carlineup\index.html',
    '\images\https_www.subaru.jp\carlineup\lowdisp.html',
    '\images\https_www.subaru.jp\cartopia',
    '\images\https_www.subaru.jp\channel',
    '\images\https_www.subaru.jp\chiffon\chiffon',
    '\images\https_www.subaru.jp\comparison',
    '\images\https_www.subaru.jp\comparison\\3d_component',
    '\images\https_www.subaru.jp\copyright',
    '\images\https_www.subaru.jp\crossover7\crossover7',
    '\images\https_www.subaru.jp\crossover7\crossover7\\3d_component\\top',
    '\images\https_www.subaru.jp\cycleroadrace',
    '\images\https_www.subaru.jp\diaswagon\diaswagon',
    '\images\https_www.subaru.jp\e-catalog',
    '\images\https_www.subaru.jp\ecocar\lineup\levorg',
    '\images\https_www.subaru.jp\ecocar\lineup\outback',
    '\images\https_www.subaru.jp\ecocar\lineup\\xv',
    '\images\https_www.subaru.jp\event',
    '\images\https_www.subaru.jp\\faq',
    '\images\https_www.subaru.jp\\forester\\forester',
    '\images\https_www.subaru.jp\\forester\\forester\\3d_component\\top',
    '\images\https_www.subaru.jp\\forester\smartedition',
    '\images\https_www.subaru.jp\golf',
    '\images\https_www.subaru.jp\grouplink',
    '\images\https_www.subaru.jp\impreza\g4',
    '\images\https_www.subaru.jp\impreza\g4\\3d_component\\top',
    '\images\https_www.subaru.jp\impreza\impreza',
    '\images\https_www.subaru.jp\impreza\impreza\\3d_component\grade',
    '\images\https_www.subaru.jp\impreza\impreza\\3d_component\\top',
    '\images\https_www.subaru.jp\impreza\impreza\design\exterior.html',
    '\images\https_www.subaru.jp\impreza\impreza\design\interior.html',
    '\images\https_www.subaru.jp\impreza\impreza\driving\platform.html',
    '\images\https_www.subaru.jp\impreza\impreza\driving\powerunit.html',
    '\images\https_www.subaru.jp\impreza\impreza\grade',
    '\images\https_www.subaru.jp\impreza\impreza\safety\safety0.html',
    '\images\https_www.subaru.jp\impreza\impreza\safety\safety1.html',
    '\images\https_www.subaru.jp\impreza\impreza\safety\safety2.html',
    '\images\https_www.subaru.jp\impreza\impreza\safety\safety3.html',
    '\images\https_www.subaru.jp\impreza\impreza\spec',
    '\images\https_www.subaru.jp\impreza\impreza\special\concept.html',
    '\images\https_www.subaru.jp\impreza\impreza\special\movie.html',
    '\images\https_www.subaru.jp\impreza\impreza\special\photo.html',
    '\images\https_www.subaru.jp\impreza\impreza\special\\reason.html',
    '\images\https_www.subaru.jp\impreza\impreza\special\special.html',
    '\images\https_www.subaru.jp\impreza\impreza\special\\voice.html',
    '\images\https_www.subaru.jp\impreza\impreza\\utility\equipment.html',
    '\images\https_www.subaru.jp\impreza\impreza\\utility\package.html',
    '\images\https_www.subaru.jp\index.html_viewmode=p',
    '\images\https_www.subaru.jp\information',
    '\images\https_www.subaru.jp\justy\justy',
    '\images\https_www.subaru.jp\legacy\\b4',
    '\images\https_www.subaru.jp\legacy\\b4\\3d_component\\top',
    '\images\https_www.subaru.jp\legacy\outback',
    '\images\https_www.subaru.jp\legacy\outback\\3d_component\grade',
    '\images\https_www.subaru.jp\legacy\outback\\3d_component\\top',
    '\images\https_www.subaru.jp\legacy\outback\design\exterior.html',
    '\images\https_www.subaru.jp\legacy\outback\design\interior.html',
    '\images\https_www.subaru.jp\legacy\outback\driving',
    '\images\https_www.subaru.jp\legacy\outback\grade',
    '\images\https_www.subaru.jp\legacy\outback\safety\safety0.html',
    '\images\https_www.subaru.jp\legacy\outback\safety\safety1.html',
    '\images\https_www.subaru.jp\legacy\outback\safety\safety2.html',
    '\images\https_www.subaru.jp\legacy\outback\safety\safety3.html',
    '\images\https_www.subaru.jp\legacy\outback\spec',
    '\images\https_www.subaru.jp\legacy\outback\special\movie.html',
    '\images\https_www.subaru.jp\legacy\outback\special\photo.html',
    '\images\https_www.subaru.jp\legacy\outback\\utility\cargoroom.html',
    '\images\https_www.subaru.jp\legacy\outback\\utility\equipment.html',
    '\images\https_www.subaru.jp\legacy\\touringwagon',
    '\images\https_www.subaru.jp\levorg\levorg',
    '\images\https_www.subaru.jp\levorg\levorg\\3d_component\grade',
    '\images\https_www.subaru.jp\levorg\levorg\\3d_component\\top',
    '\images\https_www.subaru.jp\levorg\levorg\design\exterior.html',
    '\images\https_www.subaru.jp\levorg\levorg\design\interior.html',
    '\images\https_www.subaru.jp\levorg\levorg\driving\\1.6engine.html',
    '\images\https_www.subaru.jp\levorg\levorg\driving\\2.0engine.html',
    '\images\https_www.subaru.jp\levorg\levorg\grade',
    '\images\https_www.subaru.jp\levorg\levorg\safety\safety0.html',
    '\images\https_www.subaru.jp\levorg\levorg\safety\safety1.html',
    '\images\https_www.subaru.jp\levorg\levorg\safety\safety2_1.html',
    '\images\https_www.subaru.jp\levorg\levorg\safety\safety2_2.html',
    '\images\https_www.subaru.jp\levorg\levorg\safety\safety3.html',
    '\images\https_www.subaru.jp\levorg\levorg\spec',
    '\images\https_www.subaru.jp\levorg\levorg\special\movie.html',
    '\images\https_www.subaru.jp\levorg\levorg\special\photo.html',
    '\images\https_www.subaru.jp\levorg\levorg\\utility\equipment.html',
    '\images\https_www.subaru.jp\levorg\levorg\\utility\package.html',
    '\images\https_www.subaru.jp\levorg\stisport',
    '\images\https_www.subaru.jp\levorg\stisport\\3d_component\\top',
    '\images\https_www.subaru.jp\lifeactive',
    '\images\https_www.subaru.jp\lifeactive\\about',
    '\images\https_www.subaru.jp\lifeactive\\activelifefes',
    '\images\https_www.subaru.jp\lifeactive\programs\\rally_hokkaido',
    '\images\https_www.subaru.jp\mynumber_policy',
    '\images\https_www.subaru.jp\\nbr_mechanic\\2014',
    '\images\https_www.subaru.jp\\news',
    '\images\https_www.subaru.jp\\news\\rss',
    '\images\https_www.subaru.jp\onair',
    '\images\https_www.subaru.jp\pleo\pleo',
    '\images\https_www.subaru.jp\pleoplus\pleoplus',
    '\images\https_www.subaru.jp\pleovan\pleovan',
    '\images\https_www.subaru.jp\privacy_policy',
    '\images\https_www.subaru.jp\privacy_policy\index.html',
    '\images\https_www.subaru.jp\purchase',
    '\images\https_www.subaru.jp\purchase\card',
    '\images\https_www.subaru.jp\purchase\estimate',
    '\images\https_www.subaru.jp\purchase\index.html',
    '\images\https_www.subaru.jp\purchase\insurance',
    '\images\https_www.subaru.jp\purchase\insurance\eyesight.html',
    '\images\https_www.subaru.jp\safety',
    '\images\https_www.subaru.jp\safety\eyesight',
    '\images\https_www.subaru.jp\safety\\function',
    '\images\https_www.subaru.jp\safety\index.html',
    '\images\https_www.subaru.jp\safety\lineup',
    '\images\https_www.subaru.jp\safety\\total\\active.html',
    '\images\https_www.subaru.jp\safety\\total\passive.html',
    '\images\https_www.subaru.jp\safety\\total\pre-crush.html',
    '\images\https_www.subaru.jp\safety\\total\primary.html',
    '\images\https_www.subaru.jp\safety\\voice',
    '\images\https_www.subaru.jp\saiyo',
    '\images\https_www.subaru.jp\sambar\\truck',
    '\images\https_www.subaru.jp\sambar\\van',
    '\images\https_www.subaru.jp\showroom',
    '\images\https_www.subaru.jp\sitemap',
    '\images\https_www.subaru.jp\ski',
    '\images\https_www.subaru.jp\socialmedia_policy',
    '\images\https_www.subaru.jp\stella\stella',
    '\images\https_www.subaru.jp\stisport',
    '\images\https_www.subaru.jp\subaru',
    '\images\https_www.subaru.jp\\tms',
    '\images\https_www.subaru.jp\\transcare',
    '\images\https_www.subaru.jp\wrx\s4',
    '\images\https_www.subaru.jp\wrx\s4\\3d_component\\top',
    '\images\https_www.subaru.jp\wrx\sti',
    '\images\https_www.subaru.jp\wrx\sti\\3d_component\\top',
    '\images\https_www.subaru.jp\\xv\\xv',
    '\images\https_www.subaru.jp\\xv\\xv\\3d_component\grade',
    '\images\https_www.subaru.jp\\xv\\xv\\3d_component\\top',
    '\images\https_www.subaru.jp\\xv\\xv\design\exterior.html',
    '\images\https_www.subaru.jp\\xv\\xv\design\interior.html',
    '\images\https_www.subaru.jp\\xv\\xv\driving\performance.html',
    '\images\https_www.subaru.jp\\xv\\xv\driving\platform.html',
    '\images\https_www.subaru.jp\\xv\\xv\driving\powerunit.html',
    '\images\https_www.subaru.jp\\xv\\xv\grade',
    '\images\https_www.subaru.jp\\xv\\xv\safety\safety0.html',
    '\images\https_www.subaru.jp\\xv\\xv\safety\safety1.html',
    '\images\https_www.subaru.jp\\xv\\xv\safety\safety2.html',
    '\images\https_www.subaru.jp\\xv\\xv\safety\safety3.html',
    '\images\https_www.subaru.jp\\xv\\xv\spec',
    '\images\https_www.subaru.jp\\xv\\xv\special\concept.html',
    '\images\https_www.subaru.jp\\xv\\xv\special\movie.html',
    '\images\https_www.subaru.jp\\xv\\xv\special\photo.html',
    '\images\https_www.subaru.jp\\xv\\xv\special\wp.html',
    '\images\https_www.subaru.jp\\xv\\xv\\utility\equipment.html',
    '\images\https_www.subaru.jp\\xv\\xv\\utility\package.html',
    '\images\https_www.subaru.jp\index.html_viewmode=p',
    '\images\https_www.subaru.jp\yourstorywith',
    '\images\https_www.subaru.jp'
]

def compare_image():
    text_file = open(os.path.join(header_out, 'output.syslog'), 'a')
    for i in range(len(path)):
        print(i)
        imageA = cv2.imread(os.path.join(header_A + path[i], 'a.png'), 1)
        imageB = cv2.imread(os.path.join(header_B + path[i], 'a.png'), 1)

        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

        (score, diff) = compare_ssim(grayA, grayB, full=True, multichannel=True)
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

compare_image()
print("Process Done")
