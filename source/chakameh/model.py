# -*- coding: utf-8 -*-
'''
Created on:    Dec 29, 2013
@author:        vahid
'''

from elixir import Entity,metadata,Field,Unicode,Integer,UnicodeText,session,setup_all,Binary
import md5
from reader import AudioFile

metadata.bind = "sqlite:///../../data/tracks.sqlite"
metadata.bind.echo = False

class FileExistsException(Exception):
    def __init__(self,filename):
        Exception.__init__(self,'File already exists: %s' % filename)

class Track(Entity):
    title = Field(Unicode(100))
    artist = Field(Unicode(100))
    album = Field(Unicode(100))
    composer = Field(Unicode(100))
    year = Field(Integer)
    lyricist = Field(Unicode(100))
    genere = Field(Unicode(100))
    comment = Field(UnicodeText)
    filename = Field(Unicode(500)) # Relative to archive directpory 
    filemd5 = Field(Binary(16),nullable=False,unique=True,index=True)
    
    @classmethod
    def fromfile(cls,filename):
        with open(filename) as f:
            hash = md5.md5(f.read()).digest()
        
        if cls.query.filter(cls.filemd5 == hash).first():
            raise FileExistsException(filename)
        
        reader = AudioFile(filename)
#         newtrack = cls()
#         newtrack.title = reader.title
#         newtrack.artist = reader.artist
#         newtrack.album = reader.album
#         newtrack.composer = reader.composer
#         newtrack.year = int(reader.year) if reader.year else None
#         newtrack.lyricist = reader.lyricist
#         newtrack.genere = reader.genere
#         newtrack.commebt = reader.comment
#         newtrack.filename = filename
#         newtrack.filemd5 = hash
#         
#         session.commit()
#         return newtrack
        
    
    def __repr__(self):
        return '<Track "%s" (%s)>' % (self.title, self.year)

def setup():
    setup_all(create_tables=True)


