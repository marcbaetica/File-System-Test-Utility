import os
from commands.Command import Command


class RenameFileCommand(Command):
    def __init__(self, source, destination):
        self._source = source
        self._destination = destination

    def execute(self):
        os.rename(self._source, self._destination)

    def undo(self):
        os.rename(self._destination, self._source)
