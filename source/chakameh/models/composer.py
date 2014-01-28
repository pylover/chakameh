# -*- coding: utf-8 -*-
'''
Created on:    Jan 21, 2014
@author:        vahid
'''

from elixir import Entity,Field,Unicode,OneToMany,session

class Composer(Entity):
    title = Field(Unicode(500),unique=True,nullable=False,index=True)
    tracks = OneToMany('Track')

    @classmethod
    def ensure(cls,title):
        if not title or title.strip()=='':
            return None
        composer = cls.query.filter(cls.title == title).first()
        if not composer:
            composer = cls(title = title)
            session.commit()
        return composer

    
    def __repr__(self):
        return '<Composer %s >' % (self.title,)
