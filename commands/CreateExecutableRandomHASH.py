import os
from commands.Command import Command
from commands.DeleteFileCommand import DeleteFileCommand


class CreateExecutableRandomHash(Command):
    def __init__(self, file_name):
        self.file_name = file_name

    def execute(self):
        with open(self.file_name, 'wb') as file:
            file.write(os.urandom(1000))
        # print(os.path.getsize(self.file_name))  # returns 1000 but size on disk is 4000

    def undo(self):
        DeleteFileCommand(self.file_name).execute()