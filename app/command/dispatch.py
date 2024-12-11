import os.path
from typing import Optional, List

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
        'echo': lambda args: Echo(args),
        'exit': lambda args: Exit(args),
        'cd': lambda args: Cd(args),
        'pwd': lambda args: Pwd(args),
        'type': lambda args: Type(args),
    }

    @classmethod
    def dispatch(cls, args: List[str]) -> Optional[Command]:
        """
        dispatch input to a spec command
        return none if no command received the input
        :param args:
        :return:
        """
        if len(args) == 0:
            return None
        cmd = args[0]
        cmd_func = cls.command_init_func.get(cmd)
        if cmd_func is not None:
            return cmd_func(args)
        cmd_exists = False
        if cmd.startswith('./') or cmd.startswith('../') or cmd.startswith('/'):
            cmd_exists = os.path.exists(cmd)
        else:
            cmd_path = find_command(cmd)
            if cmd_path is not None:
                cmd_exists = True
                args[0] = cmd_path
        if cmd_exists:
            return Delegate(args)
        return None
