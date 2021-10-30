from commands.Command import Command
from commands.DeleteFileCommand import DeleteFileCommand


class CreateFileCommand(Command):
    def __init__(self, filename, content=None):
        # super().__init__() -> when Command had an __init__ and @ABC
        self._filename = filename
        self._content = content

    def execute(self):
        # if file doesn't exist do that. Otherwise override file?
        with open(self._filename, 'w') as f:
            f.write(self._content)

    def undo(self):
        DeleteFileCommand(self._filename).execute()