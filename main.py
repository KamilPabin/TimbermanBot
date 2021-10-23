import keyboard
from mss import mss
from src.timberman.Block import Block


# keyboard.wait("s")

with mss() as sct:
    fourth_block = Block(sct, 1)
