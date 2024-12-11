import sys

from app.dispatch import CommandDispatcher


def main():
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
            command = CommandDispatcher.dispatch(input_str)
        except ValueError as e:
            print(e)
            continue
        if command is None:
            print(f'{input_str}: command not found')
            continue
        command.execute()


if __name__ == "__main__":
    main()
