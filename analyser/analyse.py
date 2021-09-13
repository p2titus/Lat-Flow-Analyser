import cv2 as cv


def __mask_img(img):
    thresh = 128  # we use an arbitrary threshold for now
    return cv.threshold(img, thresh, 255, cv.THRESH_BINARY)[1]


def __count_bars(img):
    return 1


def analyse(load_imgs):
    imgs = load_imgs()
    bw_imgs = map(__mask_img, imgs)
    bars = map(__count_bars, bw_imgs)

