# -*- coding: utf-8 -*-
'''
Created on:    Dec 29, 2013
@author:        vahid
'''

from elixir import Entity,Field,Unicode,Integer,UnicodeText,Binary,ManyToOne,session
from artist import Artist
from composer import Composer
from lyricist import Lyricist
from genere import Genere
from category import Category
from kivy.adapters.models import SelectableDataItem

class Track(Entity,SelectableDataItem):
    code = Field(Unicode(50),unique=True,index=True,nullable=False) 
    title = Field(Unicode(500))
    prime = Field(Unicode(500))
    artist = ManyToOne(Artist,required=False)
    composer = ManyToOne(Composer,required=False,lazy=True,
                         primaryjoin=lambda: Composer.id == Track.composer_id,
                         foreign_keys=lambda: [Track.composer_id])
    genere = ManyToOne(Genere,required=False)
    category = ManyToOne(Category,required=False)
    lyricist = ManyToOne(Lyricist,required=False)
    album = Field(Unicode(500),required=False)
    year = Field(Integer,nullable=True)
    mediano = Field(Integer,nullable=False)
    comment = Field(UnicodeText,nullable=True)
    filename = Field(Unicode(500),nullable=True) # Relative to archive directpory 
    filemd5 = Field(Binary(16),nullable=True) #,unique=True,index=True)
    language = Field(Unicode(100),nullable=True)
    
    @classmethod
    def ensure(cls,code,prime,**kw):
        kw['code'] = code
        kw['prime'] = prime
        if 'title' not in kw:
            kw['title'] = prime
         
        track = cls.query.filter(cls.code == code).first()
        if not track:
            track = cls(**kw)
        else:
            track.from_dict(kw)
        
        session.commit()
        
        return track
    
    
    def __repr__(self):
        return '<Track "%s" (%s)>' % (self.title, self.code)

