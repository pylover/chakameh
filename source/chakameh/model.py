# -*- coding: utf-8 -*-
'''
Created on:    Dec 29, 2013
@author:        vahid
'''

from elixir import Entity,metadata,Field,Unicode,Integer,UnicodeText

metadata.bind = "sqlite:///tracks.sqlite"
metadata.bind.echo = True

class Track(Entity):
    title = Field(Unicode(100))
    performer = Field(Unicode(100))
    album = Field(Unicode(100))
    year = Field(Integer)
    description = Field(UnicodeText)
    
    def __repr__(self):
        return '<Track "%s" (%d)>' % (self.title, self.year)