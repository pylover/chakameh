# -*- coding: utf-8 -*-
'''
Created on:    Jan 21, 2014
@author:        vahid
'''

from elixir import Entity,Field,Unicode,OneToMany,session

class Category(Entity):
    title = Field(Unicode(500),unique=True,nullable=False,index=True)
    tracks = OneToMany('Track')

    @classmethod
    def ensure(cls,title):      
        if not title or title.strip()=='':
            return None
        cat = Category.query.filter(Category.title == title).first()
        if not cat:
            cat = Category(title = title)
            session.commit()
        return cat
        
        
    def __repr__(self):
        return '<Category %s >' % (self.title,)
