import keyboard

from src.timberman.Logger import Logger
from src.timberman.Tree import Tree
from src.timberman.TreeSide import LeftSide


class TimberMan:

    LOGGER: Logger = Logger.get_logger("TimberMan")

    def __init__(self):
        self.__side = LeftSide()

    def chop_tree(self, tree: Tree):
        self.__side = self.__side.next_move(tree)
        TimberMan.LOGGER.print(f"My next move is {str(self.__side)}")
        keyboard.send(self.__side.get_button(), do_press=True, do_release=True)
        tree.chop()
