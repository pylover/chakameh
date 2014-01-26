# -*- coding: utf-8 -*-
'''
Created on:    Jan 21, 2014
@author:        vahid
'''

from elixir import Entity,Field,Unicode,OneToMany,session

class Genere(Entity):
    title = Field(Unicode(500),unique=True,nullable=False,index=True)
    tracks = OneToMany('Track')
    
    @classmethod
    def add_genere(cls,title):
        if not title or title.strip()=='':
            return None
        genere = cls.query.filter(cls.title == title).first()
        if not genere:
            genere = cls(title = title)
            session.commit()
        return genere
    
    
    def __repr__(self):
        return '<Genere "%s" (%s)>' % (self.title,self.id)
