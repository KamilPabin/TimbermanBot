from src.timberman.Tree import Tree


class TreeSide:

    def next_move(self, tree: Tree):
        raise NotImplementedError()

    def get_button(self) -> str:
        raise NotImplementedError()


class LeftSide(TreeSide):

    def get_button(self) -> str:
        return 'a'

    def next_move(self, tree: Tree) -> TreeSide:
        if not tree.has_branch(1):
            return self
        if tree.has_branch_on_left(1):
            return RightSide()
        return self

    def __str__(self) -> str:
        return "Left"


class RightSide(TreeSide):

    def get_button(self) -> str:
        return 'l'

    def next_move(self, tree: Tree) -> TreeSide:
        if not tree.has_branch(1):
            return self
        if tree.has_branch_on_right(1):
            return LeftSide()
        return self

    def __str__(self) -> str:
        return "Right"
