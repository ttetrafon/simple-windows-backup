import os, shutil
from pathlib import Path
from typing import List

source_directories: List[str] = [
  'C:/Users/ttetr/.aws',
  'C:/Users/ttetr/AppData/LocalLow/ZAUM Studio',
  'C:/Users/ttetr/AppData/Roaming/Blender Foundation/Blender',
  'C:/Users/ttetr/AppData/Roaming/endless-sky/saves'
]
source_files: List[str] = [
  'C:/Users/ttetr/AppData/Roaming/Code/User/settings.json',
  'C:/Users/ttetr/AppData/Roaming/endless-sky/preferences.txt'
]
target_directory: str = 'C:/Users/ttetr/OneDrive/Backup/automated'


def main() -> None:
  for file in source_files:
    source = Path(file)
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
