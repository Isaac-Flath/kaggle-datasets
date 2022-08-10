from fastkaggle.core import *
from fastcore.all import *
from pathlib import Path
import os
import time



if __name__ == '__main__':
    path = Path.home()/'.kaggle'
    os.mkdir(path)    
    
    with open(path/'kaggle.json', 'w') as f: f.write(os.environ['key'])

    libs = L(open('libraries.txt').read().split('\n')).filter(lambda x: x != '')
    lib_path = Path('./kaggle_datasets')
    
#    create_libs_datasets(libs,lib_path=lib_path,username='isaacflath',clear_after=False)

    create_f = bind(create_libs_datasets,lib_path=lib_path,username='isaacflath',clear_after=True)
    
    def tryf(lib,tries):
        for i in range(tries):
            try:
                create_f(lib)
            except:
                print(f"API limit hit - sleep and retry {i} of {tries}")
                time.sleep(30)
                continue
    f = bind(tryf,tries=5)
    parallel(f,libs)
