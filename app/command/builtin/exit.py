import sys

from app.command.command import Command
from app.error.errors import ExecuteError


class Exit(Command):
    def execute(self):
        if len(self.args) > 2:
            raise ExecuteError('exit: too many arguments')
        if len(self.args) == 1 or not self.args[1].isnumeric():
            sys.exit(0)
        sys.exit(int(self.args[1]))
