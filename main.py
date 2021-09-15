import cv2 as cv
import analyser


def test_img():
    import os
    fname = 'test_lat_flow_3.jpg'
    if os.path.exists(fname):
        return cv.imread(fname)[150:1550, 450:900]
    else:
        raise FileNotFoundError('no')


if __name__ == '__main__':
    f = lambda: [test_img()]
    analysed = analyser.analyse(f, debug=False)
    print(analysed)

