import cv2 as cv
import numpy as np
import pytesseract as ocr

def __test_show(img):
    cv.imshow('test show', img)
    cv.waitKey(0)
    exit(70)


def __grey_img(img):
    # __test_show(img)
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)


def __detect_contours(img):
    ret, thresh = cv.threshold(img, 160, 255, 0)
    contours, hier = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # __test_show(thresh)
    return thresh, contours


def __draw_rect(img_cont):
    img, points = img_cont
    rects = cv.drawContours(img, points, -1, (0, 255, 0), 3)
    # __test_show(rects)
    return rects


def __recog_text(img):
    ocr.pytesseract.tesseract_cmd = r""
    print(ocr.image_to_string(img))
    exit(71)


def analyse(load_imgs, debug=False):
    imgs = load_imgs()
    greys = map(__grey_img, imgs)
    img_cont = map(__detect_contours, greys)
    drawn = map(__draw_rect, img_cont)
    chars = map(__recog_text, drawn)

    return list(chars)

