import sys
import time
import keyboard
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

save_printscreen = True


def stop_program():
    sys.exit(1)

def save_screenshot(msg: str, image: Image):
    if save_printscreen:
        image.save(f"{msg}.png")


keyboard.on_press_key("x", lambda _: stop_program())


keyboard.wait('s')
print("started")
left_background = ImageGrab.grab(bbox=left_branch_bounding_box)
right_background = ImageGrab.grab(bbox=right_branch_bounding_box)

save_screenshot("left", left_background)
save_screenshot("right", right_background)
side = 0
i = 0
while True:
    ImageGrab.grab().save(f"fullscreen{i}.png")
    if side == 0:
        im = ImageGrab.grab(bbox=left_branch_bounding_box)
        save_screenshot(i, im)
        is_occupied = list(left_background.getdata()) != list(im.getdata())
        print(f"{i}: side: {side} is occupied: {is_occupied}")
        if is_occupied:
            side = 1
            keyboard.write("l")
        else:
            keyboard.write("a")
    else:
        im = ImageGrab.grab(bbox=right_branch_bounding_box)
        save_screenshot(i, im)
        is_occupied = list(right_background.getdata()) != list(im.getdata())
        print(f"{i}: side: {side} is occupied: {is_occupied}")
        if is_occupied:
            side = 0
            keyboard.write("a")
        else:
            keyboard.write("l")
    i = i + 1
    time.sleep(0.1)
