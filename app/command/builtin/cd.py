import os

from app.command.command import Command
from app.error.errors import ExecuteError


class Cd(Command):
    def execute(self) -> bool:
        if len(self.args) == 1:
            os.chdir(os.getcwd())
            return True
        if (len(self.args)) > 2:
            raise ExecuteError('cd: too many arguments')

        path = self.args[1]
        absolute_path = path
        if path.startswith('~'):
            absolute_path = os.path.expanduser(path)
        elif not path.startswith('/'):
            absolute_path = path

        if os.path.exists(absolute_path):
            os.chdir(absolute_path)
            return
        raise ExecuteError(f'cd: {path}: No such file or directory')
