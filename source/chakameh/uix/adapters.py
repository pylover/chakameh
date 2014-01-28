# -*- coding: utf-8 -*-
'''
Created on:    Jan 23, 2014
@author:        vahid
'''
from kivy.adapters.listadapter import ListAdapter
from chakameh.models import Composer,Lyricist,Artist,Genere,Track 


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
        
    def get_count(self):
        return len(self.data)    
        

class ComposerAdapter(BaseAdapter):
    def fetch_data(self,**kwargs):
        return Composer.query.order_by(Composer.title).all()
    
class LyricistAdapter(BaseAdapter):
    def fetch_data(self,**kwargs):
        return Lyricist.query.order_by(Lyricist.title).all()
    
class ArtistAdapter(BaseAdapter):
    def fetch_data(self,**kwargs):
        return Artist.query.order_by(Artist.title).all()
            
    def get_count(self):
        return len(self.data)

class GenereAdapter(BaseAdapter):
    def fetch_data(self,**kwargs):
        return Genere.query.order_by(Genere.title).all()

class TrackAdapter(BaseAdapter):
        
    def __init__(self,*args,**kw):
        self.filters = {}
        super(TrackAdapter,self).__init__(*args,**kw)
        
    def fetch_data(self,**kwargs):
        
        q = Track.query.order_by(Track.title)

        for key, model in self.filters.items():
            if key == 'Search':
                if model and len(model.strip()):
                    if model[0].isdigit():
                        q = q.filter(Track.code.contains(model))
                    else:
                        q = q.filter(Track.prime.contains(model))
            elif isinstance(model,Artist):
                q = q.filter(Track.artist == model)
            elif isinstance(model,Composer):
                q = q.filter(Track.composer == model)
            elif isinstance(model,Lyricist):
                q = q.filter(Track.lyricist == model)
            elif isinstance(model,Genere):
                q = q.filter(Track.genere == model)
                
        if 'limit' in kwargs:
            q = q.limit(kwargs['limit'])
            
        return q.all()
        
    def clear_filters(self):
        self.filters = {}
    
    def filter(self,model):
        self.clear_filters()
        if model:
            self.filters[model.__class__.__name__] = model
        self.data = self.fetch_data()
            
    def search(self,value):
        self.clear_filters()
        self.filters['Search'] = value.decode('utf8')
        self.data = self.fetch_data()
    
    def get_header(self):
        return [Track(title=u'عنوان',
                     composer=Composer(title=u'آهنگساز'))]
