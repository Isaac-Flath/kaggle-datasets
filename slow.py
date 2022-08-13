from fastkaggle.core import *
from fastcore.all import *
from pathlib import Path
import os
import time

if __name__ == '__main__':
    path = Path.home()/'.kaggle'
    
    if not path.exists():
        os.mkdir(path)    
        with open(path/'kaggle.json', 'w') as f: f.write(os.environ['key'])

    libs = L(open('libraries_slow.txt').read().split('\n')).filter(lambda x: x != '')
    lib_path = Path('./kaggle_datasets')
    
    for lib in libs:
        try:
            create_libs_datasets(lib,lib_path=lib_path,username='isaacflath',clear_after=False)
        except:
            print('API limit hit - 30 second hold')
            time.sleep(30)
            create_libs_datasets(lib,lib_path=lib_path,username='isaacflath',clear_after=False)
