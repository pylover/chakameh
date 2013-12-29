# -*- coding: utf-8 -*-
'''
Created on:    Dec 29, 2013
@author:        vahid
'''

import id3reader
import os

class MP3Reader(id3reader.Reader):
    def __init__(self,f):
        id3reader.Reader.__init__(self, f)
    
    @property
    def title(self):
        return self.getValue('title')
    
    @property
    def album(self):
        return self.getValue('album')

    @property
    def artist(self):
        return self.getValue('performer')

    @property
    def composer(self):
        return self.getValue('composer')
    
    @property
    def year(self):
        return self.getValue('year')
    
    @property
    def lyricist(self):
        return self.getValue('TEXT')
    
    @property
    def genere(self):
        return self.getValue('genere')    
    
    def __repr__(self):
#         if self.frames:
#             return str(self.frames.keys())
#         else:
#             return '\n'
        return u'%s\t%s\t%s\t%s\t%s\t%s\t%s' % (self.album,self.artist,self.composer,self.year,self.title,self.lyricist,self.genere)

def run(directory):
    for root, _subFolders, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp3'):
                reader = MP3Reader(os.path.join(root,file))
                print( unicode(reader))
                
        

if __name__ == '__main__':
    run('../../archive')