from PIL import Image
from mss.screenshot import ScreenShot

from src.timberman.Logger import Logger


class Branch:
    logger = Logger.get_logger("Branch")

    def __init__(self, screenshot: ScreenShot, name: str):
        im = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "RGBX").convert('L').point(lambda p: p > 7 and 255)
        Branch.logger.save_screenshot(name, im)
        self.__has_branch = len(list(im.getcolors())) == 2

    def has_branch(self) -> bool:
        return self.__has_branch

    def __str__(self) -> str:
        if self.__has_branch:
            return "---"
        return "   "
