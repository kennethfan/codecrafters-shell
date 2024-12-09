import os

from app.command.command import Command


class Pwd(Command):
    def execute(self):
        print(os.getcwd())
