import os.path
from typing import Optional

from app.command.builtin.cd import Cd
from app.command.builtin.echo import Echo
from app.command.builtin.exit import Exit
from app.command.builtin.pwd import Pwd
from app.command.builtin.type import Type
from app.command.command import Command
from app.command.custom.delegate import Delegate
from app.util.common import find_command


class CommandDispatcher:
    command_init_func = {
        'echo': lambda input_str, args: Echo(input_str, args),
        'exit': lambda input_str, args: Exit(input_str, args),
        'cd': lambda input_str, args: Cd(input_str, args),
        'pwd': lambda input_str, args: Pwd(input_str, args),
        'type': lambda input_str, args: Type(input_str, args),
    }

    @classmethod
    def dispatch(cls, input_str: str) -> Optional[Command]:
        """
        dispatch input to a spec command
        return none if no command received the input
        :param input_str:
        :return:
        """
        if '' == input_str.strip():
            return None
        args = input_str.split()
        cmd = args[0]
        cmd_func = cls.command_init_func.get(cmd)
        if cmd_func is not None:
            return cmd_func(input_str, args)
        cmd_exists = False
        if cmd.startswith('./') or cmd.startswith('../') or cmd.startswith('/'):
            cmd_exists = os.path.exists(cmd)
        else:
            cmd_path = find_command(cmd)
            if cmd_path is not None:
                cmd_exists = True
                args[0] = cmd_path
        if cmd_exists:
            return Delegate(input_str, args)
        return None
