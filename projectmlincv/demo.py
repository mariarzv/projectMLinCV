import os
from yolov5_tflite_image_inference import detect_image
from utils import getprojdir

print(getprojdir())

imgbig = os.path.normpath(getprojdir() + '/images/peoplebig.png')
weights = os.path.normpath(getprojdir() + '/weights/yolov5s-fp16.tflite')


def inf_image():
    detect_image(
        weights,
        imgbig,
        416,
        0.25,
        0.45)


inf_image()