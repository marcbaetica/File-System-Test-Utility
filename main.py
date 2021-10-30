import time
from shutil import copy

from History import History
from commands.CreateExecutableRandomHASH import CreateExecutableRandomHash
from commands.CreateRandomExecFromFile import CreateRandomExecFromFile
from commands.CreateFileCommand import CreateFileCommand
from commands.DeleteFileCommand import DeleteFileCommand
from commands.ReadFileCommand import ReadFileCommand
from commands.RenameFileCommand import RenameFileCommand


history = History()
start_time = time.perf_counter()

print(f'{time.perf_counter() - start_time:0.4f}')
history.execute(CreateFileCommand('some_test_file', 'blurb'))
history.undo()
history.execute(CreateFileCommand('some_test_file', 'blurb'))
history.execute(RenameFileCommand('some_test_file', 'some_test_file_2'))
history.undo()
history.execute(DeleteFileCommand('some_test_file'))
history.undo()
history.execute(CreateFileCommand('some_other_file', 'alhdasljkfad\ndlsaikjufald\nsa;lofjashdkl'))
history.execute(ReadFileCommand('some_other_file'))
history.undo()
history.execute(CreateFileCommand('some_other_file', 'extra blurb'))
history.execute(ReadFileCommand('some_other_file'))
history.execute(DeleteFileCommand('some_other_file'))

print(f'{time.perf_counter() - start_time:0.4f}')


# Testing filesystem calls bottleneck

files_count = 10000

history.execute(CreateExecutableRandomHash('my_exec.exe'))
for i in range(files_count):
    history.execute(CreateRandomExecFromFile('my_exec.exe', f'my_exec{i}.exe'))

print(f'{time.perf_counter() - start_time:0.4f}')

start_time = time.perf_counter()

for i in range(files_count):
    history.undo()

print(f'{time.perf_counter() - start_time:0.4f}')

# 15.5965
# 2.4513

# 15.5459
# 2.7549

# 15.8999
# 2.9028