import sys

from app.command.command import Command


class Exit(Command):
    def execute(self):
        sys.exit(0)
