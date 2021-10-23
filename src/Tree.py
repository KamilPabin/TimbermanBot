from typing import List

from src.Log import Log


class Tree:
    tree: List[Log]

    def __init__(self):
        self.tree = []

    def chop(self) -> Log:
        return self.tree.pop(0)

    def update(self):
        None