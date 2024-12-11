import os
import sys

from app.command.dispatch import CommandDispatcher
from app.error.errors import TokenError, ExecuteError
from app.util.tokenizer import Tokenizer


class CommandRunner:
    def __init__(self):
        self._pid = 0
        self._last_sub_pid = 0
        self._last_status = 0
        self._last_arg = None

    def system_variables(self):
        """
        return system variables
        """
        return {
            '$$': self._pid,
            '$!': self._last_sub_pid,
            '$?': self._last_status,
            '!$': self._last_arg,
        }

    def run(self):
        self._pid = os.getpid()
        while True:
            # Uncomment this block to pass the first stage
            sys.stdout.write("$ ")
            sys.stdout.flush()

            # Wait for user input
            while True:
                input_str = input()
                input_str = input_str.strip()
                if input_str == '':
                    continue
                break
            try:
                token_list = Tokenizer(input_str).tokenize()
                command = CommandDispatcher.dispatch(token_list)
            except TokenError as e:
                print(e)
                continue
            if command is None:
                print(f'{token_list[0]}: command not found')
                continue
            try:
                self._last_sub_pid = 0
                self._last_arg = token_list[len(token_list) - 1]
                command.execute()
                self._last_status = 0
            except ExecuteError as e:
                self._last_status = 1
                print(e)
