import os

from app.command.command import Command
from app.error.errors import ExecuteError


class Pwd(Command):
    def execute(self):
        if len(self.args) > 1:
            raise ExecuteError('pwd: too many arguments')
        print(os.getcwd())
