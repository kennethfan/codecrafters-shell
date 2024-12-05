import sys


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
    valid_commands = [exit_command]
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
        print(f'{command}: command not found')


if __name__ == "__main__":
    main()
