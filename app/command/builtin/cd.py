import os

from app.command.command import Command


class Cd(Command):
    def execute(self):
        if len(self.args) == 1:
            os.chdir(os.getcwd())
            return
        if (len(self.args)) > 2:
            print('cd: too many arguments')
            return

        path = self.args[1]
        absolute_path = path
        if path.startswith('~'):
            absolute_path = os.path.expanduser(path)
        elif not path.startswith('/'):
            absolute_path = path

        if os.path.exists(absolute_path):
            os.chdir(absolute_path)
            return
        print(f'no such file or directory: {path}')
