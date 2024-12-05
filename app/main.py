import sys
import os


def get_paths():
    path = os.getenv('PATH')
    if path == '':
        return []
    return path.split(':')


def find_command(command: str, paths: list):
    for path in paths:
        if not os.path.exists(path):
            continue
        for _, _, files in os.walk(path):
            if command in files:
                return os.path.join(path, command)
    return None


def echo_command(command: str):
    if command == 'echo':
        print('')
        return True
    if command.startswith('echo '):
        print(command[5:])
        return True
    return False


def main():
    exit_command = 'exit 0'
    valid_commands = ['echo', 'exit', 'type']
    while True:
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()
        if exit_command == command:
            sys.exit(0)
        if echo_command(command):
            continue
        if command.startswith('type '):
            command = command[5:]
            path = find_command(command, get_paths())
            if path is not None:
                print(f'{command} is {path}')
            else:
                print(f'{command}: not found')
            continue
        print(f'{command}: command not found')


if __name__ == "__main__":
    main()
