from app.command.command import Command


class Echo(Command):
    def execute(self):
        if len(self.args) == 1:
            print('')
            return
        print(self.input_str[len('echo') + 1:])
