import subprocess

from app.command.command import Command


class Delegate(Command):
    """
    a delegate for system runner, it will run the input use system runner
    """

    def execute(self):
        result = subprocess.run(self.args, capture_output=True, text=True)
        if result.stderr:
            print(result.stderr, end='')
        print(result.stdout, end='')
