# -*- coding: utf-8 -*-
'''
Created on:    Jan 21, 2014
@author:        vahid
'''

from elixir import Entity,Field,Unicode,OneToMany,session 
from chakameh.models.artable import Artable


class Artist(Entity,Artable):
    title = Field(Unicode(500),unique=True,nullable=False,index=True)
    realname = Field(Unicode(500),nullable=True)
    tracks = OneToMany('Track')
    tags = Field(Unicode(500),nullable=True)

    @classmethod
    def ensure(cls,title,realname=None):
        if not title or title.strip()=='':
            return None
        artist = cls.query.filter(cls.title == title).first()
        if not artist:
            artist = cls(title = title,realname=realname)
            session.commit()            
        return artist

    def get_arts_directory(self):
        return 'Artists'
    
    def __repr__(self):
        return '<Artist %s\t%s >' % (self.id,self.title)

