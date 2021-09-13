import cv2 as cv
import analyser

def test_img():
    import os
    fname = 'test_lat_flow.jpg'
    if os.path.exists(fname):
        return cv.imread(fname)
    else:
        raise FileNotFoundError('no')


if __name__ == '__main__':
    img = test_img()
    f = lambda: [img]
    analysed = analyser.analyse(f, debug=False)
    print(analysed)

