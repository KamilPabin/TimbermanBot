from src.Branch import Branch


class Log:
    branch: Branch

    def get_chop_direction(self) -> str:
        if self.branch == Branch.LEFT:
            return 'l'
        if self.branch == Branch.RIGHT:
            return 'a'
        if self.branch == Branch.NONE:
            return 'a'
        if self.branch == Branch.UNKNOWN:
            return 'l'
