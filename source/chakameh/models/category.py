# -*- coding: utf-8 -*-
'''
Created on:    Feb 3, 2014
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
        category = cls.query.filter(cls.title == title).first()
        if not category:
            category = cls(title = title)
            session.commit()
        return category

    
    def __repr__(self):
        return '<Category %s >' % (self.title,)
