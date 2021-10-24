from mss.base import MSSBase

from src.timberman.Branch import Branch
from src.timberman.SystemProperties import SystemProperties


class Log:
    width = 150
    height = 108
    branch_width = 150
    skip_top_pixels = 15
    offset_from_log = 50

    def __init__(self, screen_handle: MSSBase, position: int):
        self.__position = position
        self.__screen_handle = screen_handle
        self.__left_branch_bounding_box = {"top": SystemProperties.screen_height - SystemProperties.tree_offset - position * Log.height + Log.skip_top_pixels,
                                           "left": SystemProperties.screen_width / 2 - Log.width / 2 - Log.branch_width, "width": Log.branch_width - Log.offset_from_log,
                                           "height": Log.height - Log.skip_top_pixels}
        self.__right_branch_bounding_box = {"top": SystemProperties.screen_height - SystemProperties.tree_offset - position * Log.height + Log.skip_top_pixels,
                                            "left": SystemProperties.screen_width / 2 + Log.width / 2 + Log.offset_from_log, "width": Log.branch_width - Log.offset_from_log,
                                            "height": Log.height - Log.skip_top_pixels}
        self.take_screenshot()

    def take_screenshot(self):
        self.__left_branch = Branch(self.__screen_handle.grab(self.__left_branch_bounding_box), f"left_{self.__position}")
        self.__right_branch = Branch(self.__screen_handle.grab(self.__right_branch_bounding_box), f"right_{self.__position}")

    def has_branch(self):
        return self.__left_branch.has_branch() or self.__right_branch.has_branch()

    def has_branch_on_left(self):
        return self.__left_branch.has_branch()

    def has_branch_on_right(self):
        return self.__right_branch.has_branch()

    def __str__(self) -> str:
        return str(self.__left_branch) + "|      |" + str(self.__right_branch)


class EmptyLog:

    def has_branch(self):
        return False

    def has_branch_on_left(self):
        return False

    def has_branch_on_right(self):
        return False

    def __str__(self) -> str:
        return "   |      |"
