from random import randint, choice
from shutil import copyfile

from commands.Command import Command
from commands.DeleteFileCommand import DeleteFileCommand

class CreateRandomExecFromFile(Command):
    def __init__(self, file_name, new_file_name):
        self.file_name = file_name
        self.new_file_name = new_file_name

    def execute(self):
        copyfile(self.file_name, self.new_file_name)
        with open(self.new_file_name, 'a') as file:
            file.write(''.join([str(choice(range(1, 10))) for _ in range(randint(1, 10))]))
            # file.write('aaa')

    def undo(self):
        DeleteFileCommand(self.new_file_name).execute()