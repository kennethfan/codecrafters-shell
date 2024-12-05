import sys


def main():
    valid_commands = []
    while True:
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()
        if command not in valid_commands:
            print(f'{command}: command not found')
            continue


if __name__ == "__main__":
    main()
