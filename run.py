from fastkaggle.core import *
from pathlib import Path
import os

if __name__ == '__main__':
    path = Path.home()/'.kaggle'
    os.mkdir(path)
    with open(path/'kaggle.json', 'w') as f: f.write(os.environ['KAGGLE_KEY'])

    libs = open('libraries.txt').read().split('\n')
    lib_path = Path('./kaggle_datasets')
    create_libs_datasets(libs,lib_path,username)
