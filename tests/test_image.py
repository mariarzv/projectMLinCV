import pytest
import os
from yolov5_tflite_inference import Yolov5Tflite
from yolov5_tflite_image_inference import detect_image
import argparse

projdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
imgbig = os.path.normpath(projdir + '/peoplebig.png')
imgsmall = os.path.normpath(projdir + '/peoplesmall.png')


parser = argparse.ArgumentParser()
parser.add_argument(
    '-w',
    '--weights',
    type=str,
    default='yolov5s-fp16.tflite',
    help='model.pt path(s)')
parser.add_argument('--img_size', type=int, default=416, help='image size')
parser.add_argument(
    '--conf_thres',
    type=float,
    default=0.25,
    help='object confidence threshold')
parser.add_argument(
    '--iou_thres',
    type=float,
    default=0.45,
    help='IOU threshold for NMS')

opt = parser.parse_known_args()

@pytest.mark.bigimage
def test_noerror_big():
    with pytest.raises(Exception):
        detect_image(
            opt.weights,
            imgbig,
            opt.img_size,
            opt.conf_thres,
            opt.iou_thres)

@pytest.mark.smallimage
def test_noerror_small():
    with pytest.raises(Exception):
        detect_image(
            opt.weights,
            imgsmall,
            opt.img_size,
            opt.conf_thres,
            opt.iou_thres)
