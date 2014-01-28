# -*- coding: utf-8 -*-
'''
Created on:    Jan 21, 2014
@author:        vahid
'''
from elixir import Entity,Field,Unicode,OneToMany,session

class Lyricist(Entity):
    title = Field(Unicode(500),unique=True,nullable=False,index=True)
    tracks = OneToMany('Track')
    
    @classmethod
    def ensure(cls,title):
        if not title or title.strip()=='':
            return None
        lyricist = cls.query.filter(Lyricist.title == title).first()
        if not lyricist:
            lyricist = cls(title = title)
            session.commit()
        return lyricist 
    
    def __repr__(self):
        return '<Lyricist "%s" (%s)>' % (self.title,self.id)
