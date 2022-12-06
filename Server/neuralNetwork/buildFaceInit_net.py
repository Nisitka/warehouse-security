# построение нейронной сети для распознования лиц сотрудников

import os.path
import numpy as np
from PIL import Image


def pil2numpy(pach) -> np.ndarray:
    img = Image.open(pach)

    np_array = np.asarray(img)
    return np_array

def numpy2pil(np_array: np.ndarray) -> Image:
    assert_msg = 'Input shall be a HxWx3 ndarray'
    assert isinstance(np_array, np.ndarray), assert_msg
    assert len(np_array.shape) == 3, assert_msg
    assert np_array.shape[2] == 3, assert_msg

    img = Image.fromarray(np_array, 'RGB')
    return img


if __name__ == '__main__':
    data = pil2numpy('faceDetectedTest1.jpg')
    print(data)

    data2 = np.asarray([[[255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255]],
                        [[255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255]],
                        [[255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255]],
                        [[255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255],
              [255, 255, 255]]])

    img = numpy2pil(data2)
    img.show()
