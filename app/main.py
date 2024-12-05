import subprocess
import sys
import os
from typing import List, Optional


def get_paths() -> List[str]:
    '''
    get all the paths
    :return:
    '''
    path = os.getenv('PATH')
    if path == '':
        return []
    return path.split(':')


def find_command(command: str) -> Optional[str]:
    paths = get_paths()
    if paths is None or len(paths) == 0:
        return None
    for path in paths:
        if not os.path.exists(path):
            continue
        for _, _, files in os.walk(path):
            if command in files:
                return os.path.join(path, command)
    return None


def echo_command(command: str) -> bool:
    if command == 'echo':
        print('')
        return True
    if command.startswith('echo '):
        print(command[5:])
        return True
    return False


def run_command(commands) -> Optional[str]:
    result = subprocess.run(commands, capture_output=True, text=True)
    if result.stderr:
        return result.stderr
    return result.stdout


def main():
    exit_command = 'exit 0'
    builtin_commands = ['echo', 'exit', 'type']
    while True:
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()
        if command.strip() == '':
            continue
        if exit_command == command:
            sys.exit(0)
        if echo_command(command):
            continue
        if command.startswith('type '):
            command = command[5:]
            if command in builtin_commands:
                print(f'{command} is a shell builtin')
            else:
                path = find_command(command)
                if path is not None:
                    print(f'{command} is {path}')
                else:
                    print(f'{command}: not found')
            continue
        commands = command.split(' ')
        path = find_command(commands[0])
        if path is not None:
            commands[0] = path
            output = run_command(commands)
            if output:
                print(output)
            continue
        print(f'{command}: command not found')


if __name__ == "__main__":
    main()
