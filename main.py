import sys
import time
import keyboard
import pyautogui as pyautogui
import numpy as np
import cv2
from mss import mss

from PIL import ImageGrab

# 0, 0      720, 0     1440, 0
# 0,450     720, 450   1440,450
# 0, 90l0    720, 900   1440, 900
from PIL.Image import Image

block_height = 75
height = 900
offset_y = 280

block_width = 150
middle_x = 720
branch_width = 150

left_branch_bounding_box = (middle_x - block_width / 2 - 110, height - offset_y - block_height - 29 - 60, middle_x - block_width / 2, height - offset_y - block_height - 29)
right_branch_bounding_box = (middle_x + block_width / 2, height - offset_y - block_height - 29 - 60, middle_x + block_width / 2 + 110, height - offset_y - block_height - 29)

left_monitor = {"top": height - offset_y - block_height - 29 - 60, "left": middle_x - block_width / 2 - 110, "width": 110, "height": 60}
right_monitor = {"top": height - offset_y - block_height - 29 - 60, "left": middle_x + block_width / 2, "width": 110, "height": 60}


keyboard.wait('s')
print("started")
with mss() as sct:
    left_background = sct.grab(left_monitor)
    right_background = sct.grab(right_monitor)

    side = 0
    i = 0
    while True:
        if side == 0:
            im = sct.grab(left_monitor)
            is_occupied = list(im.raw) != list(left_background.raw)
            print(f"{i}: side: {side} is occupied: {is_occupied}")
            if is_occupied:
                side = 1
                keyboard.write("l")
            else:
                keyboard.write("a")
        else:
            im = sct.grab(right_monitor)
            is_occupied = list(im.raw) != list(right_background.raw)
            print(f"{i}: side: {side} is occupied: {is_occupied}")
            if is_occupied:
                side = 0
                keyboard.write("a")
            else:
                keyboard.write("l")
        i = i + 1
        time.sleep(0.3)

