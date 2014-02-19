# -*- coding: utf-8 -*-
'''
Created on:    Feb 5, 2014
@author:        vahid
'''
# -*- coding: utf-8 -*-
'''
Created on:    Jan 21, 2014
@author:        vahid
'''

from elixir import DateTime, Entity,Field 

class ApplicationInfo(Entity):
    last_run = Field(DateTime)
    
    @classmethod
    def single(cls):
        res = cls.query.first()
        if not res:
            res = cls()
        return res
