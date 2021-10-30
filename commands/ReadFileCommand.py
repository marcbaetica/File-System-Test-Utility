from commands.Command import Command


class ReadFileCommand(Command):
    def __init__(self, filename):
        self._filename = filename

    def execute(self):
        print(f'Contents of file [{self._filename}]:')
        with open(self._filename, 'r') as f:
            print(f.read())

    def undo(self):
        print('Undo is not supported for reading files.')