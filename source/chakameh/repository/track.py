# -*- coding: utf-8 -*-
'''
Created on:    Dec 29, 2013
@author:        vahid
'''

from elixir import Entity,Field,Unicode,Integer,UnicodeText,Binary,ManyToOne
from artist import Artist
from category import Category
from composer import Composer
from lyricist import Lyricist
from genere import Genere

class Track(Entity):
    code = Field(Unicode(50),unique=True,index=True,nullable=False) 
    title = Field(Unicode(500))
    prime = Field(Unicode(500))
    artist = ManyToOne(Artist,required=False)
    category = ManyToOne(Category)
    composer = ManyToOne(Composer,required=False)
    genere = ManyToOne(Genere,required=False)
    lyricist = ManyToOne(Lyricist,required=False)
    album = Field(Unicode(500),required=False)
    year = Field(Integer,nullable=True)
    mediano = Field(Integer,nullable=False)
    comment = Field(UnicodeText,nullable=True)
    filename = Field(Unicode(500),nullable=True) # Relative to archive directpory 
    filemd5 = Field(Binary(16),nullable=True) #,unique=True,index=True)
    
    def __repr__(self):
        return '<Track "%s" (%s)>' % (self.title, self.code)

