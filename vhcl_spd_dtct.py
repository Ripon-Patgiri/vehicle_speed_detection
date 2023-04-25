import cv2
import numpy as np
import time

# Load YOLOv7 pre-trained weights and configuration files
net = cv2.dnn.readNetFromDarknet('yolov7.cfg', 'yolov7.weights')