import os, shutil
from pathlib import Path
from typing import List

source_directories: List[str] = [
  'C:\\Users\\ttetr\\.aws',
  'C:\\Users\\ttetr\\AppData\\Roaming\\Blender Foundation\\Blender',
  'C:\\Users\\ttetr\\AppData\\LocalLow\\ZAUM Studio'
]
source_files: List[str] = [
  'C:\\Users\\ttetr\\AppData\\Roaming\\Code\\User\\settings.json'
]
target_directory: str = 'C:\\Users\\ttetr\\OneDrive\\Backup\\automated'


def main() -> None:
  for file in source_files:
    source = Path(file)
    file_root = os.path.dirname(source)[2:]
    file_name = os.path.basename(source)
    destination = Path(target_directory + file_root + '//' + file_name)
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    shutil.copy(source, destination)

  for directory in source_directories:
    None


if __name__ == '__main__':
  main()
