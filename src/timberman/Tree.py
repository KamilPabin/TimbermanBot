from mss.base import MSSBase

from src.timberman.Log import EmptyLog, Log


class Tree:

    def __init__(self, screen_handle: MSSBase):
        self.__tree = [EmptyLog(), EmptyLog(), Log(screen_handle, 3), Log(screen_handle, 4)]
        self.__screen_handle = screen_handle

    def chop(self):
        self.__tree.pop(0)

    def update(self):
        self.__tree.append(Log(self.__screen_handle, 4))

    def has_branch(self, position: int):
        return self.__tree[position].has_branch()

    def has_branch_on_left(self, position: int):
        return self.__tree[position].has_branch_on_left()

    def has_branch_on_right(self, position: int):
        return self.__tree[position].has_branch_on_right()

    def __str__(self) -> str:
        return "".join(f"{str(branch)}\n" for branch in reversed(self.__tree))
