# -*- coding: utf-8 -*-
'''
Created on:    Jan 27, 2014
@author:        vahid
'''

from kivy.app import App
from chakameh.gui.adapters import TrackAdapter
from kivy.uix.listview import CompositeListItem, ListItemButton, ListItemLabel
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.listview import ListView
import os.path

class ChakamehApp(App):
    def __init__(self):
        App.__init__(self)
        self.appdir = os.path.abspath(os.path.dirname(__file__))
        
        self.kv_files = [os.path.join(self.appdir,'views',f) for f in ['global.kv','player.kv','root.kv']]
        self.root_kv_file = os.path.join(self.appdir,'views','root.kv')

    def build(self):
        for f in self.kv_files:
            Builder.load_file(f, rulesonly=True)
                    
        listview = Builder.load_file(self.root_kv_file)
        
        listview.adapter = TrackAdapter(data=[],
          
                                     cls=CompositeListItem,
                                     propagate_selection_to_data=False,
                                     on_selection_change=self.track_selected,
                                     args_converter=lambda idx, rec:{
                                        'text': rec.title,
                                        'size_hint_y': None,
                                        'height': 32,
                                        'cls_dicts': [
                                            {'cls': ListItemButton, 'kwargs': {'text': rec.title}},
                                            {'cls': ListItemLabel, 'kwargs': {'text': "Middle-{0}".format(rec.code), 'is_representing_cls': True}},
                                            {'cls': ListItemButton, 'kwargs': {'text': str(rec.id)}}]}) 
        return listview

    def track_selected(self,*args,**kw):
        i = 0
#      source: '' if not playlistview.adapter.selection else playlistview.adapter.selection[0].parent.model.filename        
#        self.root.ids['player'].source = 

    def update_tracks(self,dt):
        pass
        #self.root.canvas.ask_update()

    def on_start(self):

        Clock.schedule_interval(self.update_tracks,1)
        
        
