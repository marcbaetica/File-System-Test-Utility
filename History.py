from commands.Command import Command


class History:
    def __init__(self):
        self._history = list()

    def execute(self, command):
        self._history.append(command)
        command.execute()

    def undo(self):
        self._history.pop().undo()
