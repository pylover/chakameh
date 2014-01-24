# -*- coding: utf-8 -*-
'''
Created on:    Jan 23, 2014
@author:        vahid
'''
from kivy.adapters.listadapter import ListAdapter
from chakameh.repository import Composer,Lyricist,Artist,Genere,Track 


class BaseAdapter(ListAdapter):
    def __init__(self,**kwargs):
        if 'data' not in kwargs:
            self.data = self.fetch_data()
            kwargs['data'] = self.data
        else:
            self.data = kwargs['data'] 
        if  'args_converter' not in kwargs:
            kwargs['args_converter'] = lambda i,obj: {'index':i,'model':obj}
        if  'template' not in kwargs:
            kwargs['template'] = 'SimpleListItem'
        super(BaseAdapter,self).__init__(**kwargs)
        
    
        

class ComposerAdapter(BaseAdapter):
    def fetch_data(self,**kwargs):
        return Composer.query.order_by(Composer.title).all()
        
    def get_count(self):
        return len(self.data)
    
class LyricistAdapter(BaseAdapter):
        
    def fetch_data(self,**kwargs):
        return Lyricist.query.order_by(Lyricist.title).all()
        
    def get_count(self):
        return len(self.data)
    
class ArtistAdapter(BaseAdapter):
    def fetch_data(self,**kwargs):
        return Artist.query.order_by(Artist.title).all()
            
    def get_count(self):
        return len(self.data)

class GenereAdapter(BaseAdapter):
    def fetch_data(self,**kwargs):
        return Genere.query.order_by(Genere.title).all()
        
    def get_count(self):
        return len(self.data)

class TrackAdapter(BaseAdapter):
    def __init__(self,**kw):
        kw['selection_limit'] = 10
        super(TrackAdapter,self).__init__(**kw)
        
    def fetch_data(self,**kwargs):
        return Track.query.order_by(Track.title).all()
        
    def get_header(self):
        return [Track(title=u'عنوان',
                     composer=Composer(title=u'آهنگساز'))]
    
    def get_count(self):
        return len(self.data)
    
    def on_selection_change(self,*args,**kw):
        i = 0

