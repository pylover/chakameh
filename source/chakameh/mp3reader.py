# -*- coding: utf-8 -*-
'''
Created on:    Dec 30, 2013
@author:        vahid
'''

import struct

# import eyed3
# 
# audiofile = eyed3.load("song.mp3")
# audiofile.tag.artist = u"Nobunny"
# audiofile.tag.album = u"Love Visions"
# audiofile.tag.title = u"I Am a Girlfriend"
# audiofile.tag.track_num = 4
# 
# audiofile.tag.save()

class MyReader(object):
    def __init__(self,filename):
        self.filename = filename
        
    def __enter__(self):
        self.file = open(self.filename,'b')
    
    def __exit__(self, type, value, traceback):
        self.file.close()
    
#    def _read
    