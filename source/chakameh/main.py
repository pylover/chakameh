# -*- coding: utf-8 -*-
'''
Created on Jan 16, 2014

@author: vahid
'''

import os
import re
import fnmatch
from chakameh.config import config

    
def start(config_filename=None):
    from kivy.lang import Builder
    from kivy.logger import Logger
    from chakameh.gui.app import ChakamehApp
    thisdir = os.path.dirname(__file__)
    
    if config_filename:
        config.load_files(config_filename)
    
    for root, _dirs, files in os.walk(thisdir):
        files = [os.path.join(root, f) for f in files if re.match(fnmatch.translate('*.kv'),f)]
        for f in files:
            Logger.debug('loading style file: %s' % f)
            Builder.load_file(f)
            
    ChakamehApp().run()    
    
if __name__ == '__main__':
    start()
    