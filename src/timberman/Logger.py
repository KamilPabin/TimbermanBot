import time

from PIL.Image import Image

from src.timberman.SystemProperties import SystemProperties


class Logger:

    def __init__(self, logging_enabled: bool, screenshot_saving_enabled: bool, name: str):
        self.__logging_enabled = logging_enabled
        self.__screenshot_saving_enabled = screenshot_saving_enabled
        self.__name = name

    def print(self, msg: str):
        if self.__logging_enabled:
            print(f"{time.time()} {self.__name}: {msg}")

    def save_screenshot(self, name: str, image: Image):
        if self.__screenshot_saving_enabled:
            image.save(f"{name}.png")

    @classmethod
    def get_logger(cls, name: str):
        return Logger(SystemProperties.logging_enabled, SystemProperties.screenshot_saving_enabled, name)
