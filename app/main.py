import sys


def main():
    exit_command = 'exit 0'
    valid_commands = [exit_command]
    while True:
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()
        if command not in valid_commands:
            print(f'{command}: command not found')
            continue
        if exit_command == command:
            sys.exit(0)


if __name__ == "__main__":
    main()
