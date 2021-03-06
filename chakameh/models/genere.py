# -*- coding: utf-8 -*-
'''
Created on:    Jan 21, 2014
@author:        vahid
'''

from elixir import Entity,Field,Unicode,OneToMany,session
from chakameh.models.artable import Artable

class Genere(Entity,Artable):
    title = Field(Unicode(500),unique=True,nullable=False,index=True)
    tracks = OneToMany('Track')
    tags = Field(Unicode(500),nullable=True)
        
    @classmethod
    def ensure(cls,title):
        if not title or title.strip()=='':
            return None
        genere = cls.query.filter(cls.title == title).first()
        if not genere:
            genere = cls(title = title)
            session.commit()
        return genere
    
    
    def __repr__(self):
        return '<Genere "%s" (%s)>' % (self.title,self.id)
