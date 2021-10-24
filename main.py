import time

import keyboard
from mss import mss

from src.timberman.TimberMan import TimberMan
from src.timberman.Tree import Tree

keyboard.wait("s")
with mss() as sct:
    timberman = TimberMan()
    tree = Tree(sct)
    while True:
        timberman.chop_tree(tree)
        time.sleep(0.06)
        tree.update()
