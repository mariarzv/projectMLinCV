import pytest
import os
import cv2
import numpy as np
from utils import getprojdir
from utils import imgresize416
from yolov5_tflite_image_inference import detect_image

img = os.path.normpath(getprojdir() + '/peoplebig.png')


def mse(image1, image2):
    # mean squared error between two images
    err = np.sum((image1.astype("float") - image2.astype("float")) ** 2)
    err /= float(image1.shape[0] * image1.shape[1])
    return err


@pytest.mark.regression
def test_image_regression():
    image1 = cv2.imread(img)
    # image1 = imgresize416(image)
    image2 = detect_image('yolov5s-fp16.tflite',
                          img,
                          416,
                          0.25,
                          0.45)

    # compare them using mse
    error = mse(image1, image2)

    # assert that the error is below a threshold
    assert error < 5000
