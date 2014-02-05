# -*- coding: utf-8 -*-
'''
Created on Jan 16, 2014

@author: vahid
'''

import os
from chakameh.config import config

thisdir = os.path.dirname(__file__)
def start(config_filename=None):
    
    if config_filename:
        config.load_files(config_filename)

    from chakameh.app import ChakamehApp
    app = ChakamehApp()        
    app.run()
    
if __name__ == '__main__':
    start()
    