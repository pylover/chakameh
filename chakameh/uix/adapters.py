# -*- coding: utf-8 -*-
'''
Created on:    Jan 23, 2014
@author:        vahid
'''
from kivy.adapters.listadapter import ListAdapter
from kivy.clock import Clock
from chakameh.models import Composer,Lyricist,Artist,Genere,Track 


class BaseAdapter(ListAdapter):
    def __init__(self,**kwargs):
        if 'data' not in kwargs:
            self.data = self.fetch_data()
            kwargs['data'] = self.data
        else:
            self.data = kwargs['data'] 
        if  'args_converter' not in kwargs:
            kwargs['args_converter'] = lambda i,obj: {'index':i,
                                                      'title': obj.title,
                                                      'entity_name': obj.__class__.__name__.lower(),
                                                      'objid': obj.id} #,'model':obj}
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
        self.sorts = []
        self._temp_data = []
        if  'args_converter' not in kw:
            kw['args_converter'] = lambda i,obj: {'index':i,
                                                  'title': obj.title,
                                                  'prime': obj.prime,
                                                  'id': obj.id,
                                                  'code': obj.code,
                                                  'entity_name': obj.__class__.__name__.lower(),
                                                  'genere': '' if not obj.genere else obj.genere.title,
                                                  'artist': '' if not obj.artist else obj.artist.title, 
                                                  'composer': '' if not obj.composer else obj.composer.title,
                                                  'lyricist': '' if not obj.lyricist else obj.lyricist.title,
                                                  'filename': '' if not obj.filename else obj.filename,
        }
        super(TrackAdapter,self).__init__(*args,**kw)
        
    def fetch_data(self,**kwargs):
        
        q = Track.query

        for key, objid in self.filters.items():
            if key == 'Search':
                if objid and len(objid.strip()):
                    if objid[0].isdigit():
                        q = q.filter(Track.code.contains(objid))
                    else:
                        q = q.filter(Track.prime.contains(objid))
            elif key == 'artist':
                q = q.filter(Track.artist_id == objid)
            elif key == 'composer':
                q = q.filter(Track.composer_id == objid)
            elif key == 'lyricist':
                q = q.filter(Track.lyricist_id == objid)
            elif key == 'genere':
                q = q.filter(Track.genere_id == objid)
                
        if 'limit' in kwargs:
            q = q.limit(kwargs['limit'])
            
        if self.sorts and len(self.sorts[0]):
            q = q.order_by(' '.join(self.sorts[0]))
            
        return q
        
    def clear_filters(self):
        self.filters = {}
    
    def _update_data(self):
        def _upd(dt):
            self.data = self.fetch_data()
        Clock.schedule_once(_upd, .1)
    
    def sort(self,column,sort_status):
        self.sorts = [(column,sort_status)] if sort_status != 'none' else []
        self._update_data()
    
    def filter(self,model,id=None):
        self.clear_filters()
        if model:
            self.filters[model] = id
        self._update_data()
        #self.data = self.fetch_data()
            
    def search(self,value):
        self.clear_filters()
        self.filters['Search'] = value.decode('utf8')
        self._update_data()
        #self.data = self.fetch_data()
    
    def get_header(self):
        return [Track(title=u'عنوان',
                     composer=Composer(title=u'آهنگساز'))]
        
    def get_count(self):
        res = super(TrackAdapter,self).get_count()
        return res
        
    def select_next_track(self):
        if len(self.selection):
            selected = self.selection[0].parent
            next = self.get_view(selected.row_index + 1)
            if not next:
                next = self.get_view(0)
            if next:
                self.selection[0].deselect()
                self.deselect_item_view(self.selection[0])
                self.select_list([next.children[1]],extend=False)
                

#     __populated = False
#     def get_view(self,index):
#         if not self.__populated:
#             print self.get_count()
#             for i in xrange(self.get_count()):
#                 super(TrackAdapter,self).get_view(i)
# 
#         return super(TrackAdapter,self).get_view(index)