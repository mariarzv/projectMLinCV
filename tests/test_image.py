import pytest
from PIL import Image
from yolov5_tflite_inference import Yolov5Tflite
from yolov5_tflite_image_inference import detect_image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-w',
    '--weights',
    type=str,
    default='yolov5s.pt',
    help='model.pt path(s)')
parser.add_argument(
    '-i',
    '--img_path',
    type=str,
    required=True,
    help='image path')
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

opt = parser.parse_args()
