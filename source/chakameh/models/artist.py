# -*- coding: utf-8 -*-
'''
Created on:    Jan 21, 2014
@author:        vahid
'''

from elixir import Entity,Field,Unicode,OneToMany,session 
from chakameh.models.artable import Artable


class Artist(Entity,Artable):
    title = Field(Unicode(500),unique=True,nullable=False,index=True)
    tracks = OneToMany('Track')

    @classmethod
    def ensure(cls,title):
        if not title or title.strip()=='':
            return None
        artist = cls.query.filter(cls.title == title).first()
        if not artist:
            artist = cls(title = title)
            session.commit()
        return artist

    # Artable methods
    def get_tags(self):
        return []
    
    def get_arts_directory(self):
        return 'Artists'
    
    def __repr__(self):
        return '<Artist %s\t%s >' % (self.id,self.title)

