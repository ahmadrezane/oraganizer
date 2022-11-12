
import json
import shutil
from pathlib import Path
from pickle import TRUE

from src.Data import DATA_DIR
from src.utils.io import read_json


class oraganizer:
    """
    this class is used to organize a directory by moving
    files into directories based on extentions.
    """
    def __init__(self, directory):
        self.directory = Path(directory)
        if not self.directory.exists():
            raise FileNotFoundError(f'{self.directory} not found')
        self.file_type_dir = read_json(DATA_DIR / 'extensions_data.json')
           
    def __call__(self):
        for file in self.directory.iterdir():
            ex = file.suffix.replace('.', '')
            if ex not in self.file_type_dir:
                continue
            else:
                DEST_DIR = self.directory / self.file_type_dir[ex][0]
                DEST_DIR.mkdir(exist_ok=TRUE)
                shutil.move(str(file), str(DEST_DIR))
                print(f'{file.name}  ----->>  {DEST_DIR}')
                


h = oraganizer('/mnt/d')
h()
