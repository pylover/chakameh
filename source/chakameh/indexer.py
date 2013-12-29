# -*- coding: utf-8 -*-
'''
Created on:    Dec 29, 2013
@author:        vahid
'''


import os
from model import Track,FileExistsException,setup as setup_model

def import_file(filename):
    pass
    
def run(directory):
    setup_model()
    for root, _subFolders, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp3'):
                try:
                    _newtrack = Track.fromfile(os.path.join(root,file))
                    print('Added: %s' % repr(_newtrack))
                except FileExistsException as ex:
                    print(ex.message)
                
        

if __name__ == '__main__':
    run('../../archive')