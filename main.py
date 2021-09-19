# Average LOC: 5.25
# Average CC: 1.25

import numpy as np
from PIL import Image


def elem_mult(img, mat):  # LOC: 1, CC: 1
    return np.einsum("ij, ...j", mat, img)


def make_colorblind(rgb, color_deficit="d"):  # LOC: 13, CC: 1
    cb_matrices = {
        "d": np.array([[1, 0, 0], [1.10104433,  0, -0.00901975], [0, 0, 1]]),
        "p": np.array([[0, 0.90822864, 0.008192], [0, 1, 0], [0, 0, 1]]),
        "t": np.array([[1, 0, 0], [0, 1, 0], [-0.15773032,  1.19465634, 0]]),
    }
    rgb2lms = np.array([[0.3904725, 0.54990437, 0.00890159],
       [0.07092586, 0.96310739, 0.00135809],
       [0.02314268, 0.12801221, 0.93605194]])
    lms2rgb = np.linalg.inv(rgb2lms)
    lms = elem_mult(rgb, rgb2lms)
    blind_lms = elem_mult(lms, cb_matrices[color_deficit])
    blind_rgb = elem_mult(blind_lms, lms2rgb)
    return blind_rgb


def colorblind_img(img_file, colorblind_type="p"):  # LOC: 4, CC: 1
    rgb_arr = np.array(Image.open(img_file).convert('RGB'))
    cb_arr = make_colorblind(rgb_arr, color_deficit=colorblind_type).astype('uint8')
    cb_img = Image.fromarray(cb_arr)
    return cb_img


def main():  # LOC: 3, CC: 2
    for c in ['d', 't', 'p']:
        img = colorblind_img('test.jpg', c)
        img.show()


if __name__ == '__main__':
    main()
