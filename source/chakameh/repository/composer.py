# -*- coding: utf-8 -*-
'''
Created on:    Jan 21, 2014
@author:        vahid
'''

from elixir import Entity,Field,Unicode,OneToMany

class Composer(Entity):
    title = Field(Unicode(500),unique=True,nullable=False,index=True)
    tracks = OneToMany('Track')

    
    def __repr__(self):
        return '<Composer %s >' % (self.title,)
