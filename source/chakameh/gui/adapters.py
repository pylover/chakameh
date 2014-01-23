# -*- coding: utf-8 -*-
'''
Created on:    Jan 23, 2014
@author:        vahid
'''
from kivy.adapters.listadapter import ListAdapter
from chakameh.repository import Composer,Lyricist,Artist,Genere 
from kivy.uix.listview import ListItemButton

def args_converter(index,obj):        
    return {'text':obj.title,
            'size_hint_y': None,
            'height': 20}


class ComposerAdapter(ListAdapter):
    def __init__(self,**kwargs):
        self.data = Composer.query.order_by(Composer.title).all()
        kwargs['data'] = self.data
        kwargs['args_converter'] = args_converter
        kwargs['cls'] = ListItemButton
        super(ComposerAdapter,self).__init__(**kwargs)
        
    def get_count(self):
        return len(self.data)
    
class LyricistAdapter(ListAdapter):
    def __init__(self,**kwargs):
        self.data = Lyricist.query.order_by(Lyricist.title).all()
        kwargs['data'] = self.data
        kwargs['args_converter'] = args_converter
        kwargs['cls'] = ListItemButton
        super(LyricistAdapter,self).__init__(**kwargs)
        
    def get_count(self):
        return len(self.data)
    
class ArtistAdapter(ListAdapter):
    def __init__(self,**kwargs):
        self.data = Artist.query.order_by(Artist.title).all()
        kwargs['data'] = self.data
        kwargs['args_converter'] = args_converter
        kwargs['cls'] = ListItemButton
        super(ArtistAdapter,self).__init__(**kwargs)
        
    def get_count(self):
        return len(self.data)

class GenereAdapter(ListAdapter):
    def __init__(self,**kwargs):
        self.data = Genere.query.order_by(Genere.title).all()
        kwargs['data'] = self.data
        kwargs['args_converter'] = args_converter
        kwargs['cls'] = ListItemButton
        super(GenereAdapter,self).__init__(**kwargs)
        
    def get_count(self):
        return len(self.data)
   