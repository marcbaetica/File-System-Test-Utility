from commands.Command import Command


class ModifyFileContentsCommand(Command):
    def __init__(self, filename, new_contents):
        self._filename = filename
        self._new_contents = new_contents

    def execute(self):
        with open(self._filename, 'w') as f:
            f.write(self._new_contents)

    def undo(self):
        print('Undo is not supported for modifying the content of files.')
