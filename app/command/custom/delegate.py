import subprocess

from app.command.command import Command
from app.error.errors import ExecuteError


class Delegate(Command):
    """
    a delegate for system runner, it will run the input use system runner
    """

    def execute(self):
        result = subprocess.run(self.args, capture_output=True, text=True)
        if 0 != result.returncode:
            if result.stderr.endswith("\n"):
                raise ExecuteError(result.stderr[0:-1])
            else:
                raise ExecuteError(result.stderr)
        print(result.stdout, end='')
