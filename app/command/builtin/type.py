from app.command.command import Command
from app.error.errors import ExecuteError
from app.util.common import find_command


class Type(Command):
    builtin_commands = ['echo', 'exit', 'type', 'pwd', 'cd']

    def execute(self):
        command = self.args[1]
        if command in self.builtin_commands:
            print(f'{command} is a shell builtin')
            return

        path = find_command(command)
        if path is not None:
            print(f'{command} is {path}')
        else:
            raise ExecuteError(f'{command}: not found')
