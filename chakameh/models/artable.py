# -*- coding: utf-8 -*-
'''
Created on:    Jan 21, 2014
@author:        vahid
'''

from chakameh.config import config
import os

def _get_media_list(directory):
    arts_dir = os.path.join(config.media_arts_root,directory)
    extensions = config.media_arts_extensions
    for dirname, _dirnames, filenames in os.walk(arts_dir):
        for filename in filenames:
            for ext in extensions:
                if filename.endswith(ext):
                    yield os.path.abspath(os.path.join(dirname, filename))
                    break

class Artable(object):
    
    def get_tags(self):
        return self.tags.split(',')
    
    def get_arts_directory(self):
        """ abstract """
        raise NotImplementedError
    
    def get_media_list(self):
        return _get_media_list(self.get_arts_directory())
    
    def get_arts(self):
        tags = self.get_tags()
        for fn in self.get_media_list():
            for tag in tags:
                if tag in fn.lower():
                    yield fn
