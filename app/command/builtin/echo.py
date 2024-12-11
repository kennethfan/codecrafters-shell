from app.command.command import Command


class Echo(Command):
    def execute(self):
        if len(self.args) == 1:
            print('')
            return
        for arg in self.args[1:]:
            print(arg, end=' ')
        print('')
