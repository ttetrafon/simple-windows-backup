import os, shutil
from pathlib import Path
from typing import List

source_directories: List[str] = []
with open('./folders.txt') as folders_input:
  source_directories = folders_input.read().splitlines()

source_files: List[str] = []
with open('./files.txt') as files_input:
  source_files = files_input.read().splitlines()

target_directory: str = 'C:/Users/ttetr/OneDrive/Backup/automated'


def main() -> None:
  for file in source_files:
    source = Path(file.strip())
    root = os.path.dirname(source)[2:]
    name = os.path.basename(source)
    destination = Path(target_directory + root + '//' + name)
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    shutil.copy(source, destination)

  for directory in source_directories:
    source = Path(directory)
    root = directory[3:]
    target = Path(target_directory)
    destination = target / root
    # destination.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, dirs_exist_ok=True)


if __name__ == '__main__':
  main()
  input("Hit Enter to finish...")
