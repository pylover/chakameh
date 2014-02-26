# -*- coding: utf-8 -*-
'''
Created on:    Jan 21, 2014
@author:        vahid
'''

from chakameh.config import config
import os


class Artable(object):
    
    def get_tags(self):
        if self.tags:
            return self.tags.split(',')
        return []
    
    def get_arts_directory(self):
        """ abstract """
        raise NotImplementedError
    
    def get_arts(self):
        arts_dir = os.path.join(config.arts.root,self.get_arts_directory())
        extensions = config.arts.extensions
        for tag in self.get_tags():
            if not tag.strip():
                break
            art_dir = os.path.join(arts_dir,tag)
            if os.path.exists(art_dir):
                for f in os.listdir(art_dir):
                    for ext in extensions:
                        if f.endswith(ext):
                            yield os.path.abspath(os.path.join(art_dir, f))
