import os
from commands.Command import Command


class DeleteFileCommand(Command):
    def __init__(self, filename):
        self._filename = filename

    def execute(self):
        os.remove(self._filename)

    def undo(self):
        print('Undo is not supported for deleting the files.')