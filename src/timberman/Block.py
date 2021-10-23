from PIL import Image
from mss.base import MSSBase
import mss.tools

from src.timberman.Logger import Logger
from src.timberman.SystemProperties import SystemProperties


class Block:
    width = 150
    height = 108
    branch_width = 150
    logger = Logger.get_logger("Block")

    def __init__(self, screen_handle: MSSBase, position: int):
        self.position = position
        self.screen_handle = screen_handle
        self.left_branch_bounding_box = {"top": SystemProperties.screen_height - SystemProperties.tree_offset - position * Block.height,
                                         "left": SystemProperties.screen_width / 2 - Block.width / 2 - Block.branch_width, "width": Block.branch_width, "height": Block.height}
        self.right_branch_bounding_box = {"top": SystemProperties.screen_height - SystemProperties.tree_offset - position * Block.height,
                                          "left": SystemProperties.screen_width / 2 + Block.width / 2, "width": Block.branch_width, "height": Block.height}
        self.take_screenshot()

    def take_screenshot(self):
        left_branch = self.screen_handle.grab(self.left_branch_bounding_box)
        right_branch = self.screen_handle.grab(self.right_branch_bounding_box)
        mss.tools.to_png(left_branch.rgb, left_branch.size, output="left.png")
        mss.tools.to_png(right_branch.rgb, right_branch.size, output="right.png")
