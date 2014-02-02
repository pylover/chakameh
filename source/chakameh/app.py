# -*- coding: utf-8 -*-
'''
Created on:    Jan 27, 2014
@author:        vahid
'''

from kivy.app import App
from kivy.lang import Builder
import os.path
import cProfile

class ChakamehApp(App):
    def __init__(self):
        App.__init__(self)
        self.appdir = os.path.abspath(os.path.dirname(__file__))
        
        self.kv_files = [os.path.join(self.appdir,'views',f) for f in ['global.kv',
                                                                       'player.kv',
                                                                       'rightpane.kv',
                                                                       'playlist.kv',
                                                                       'mediaart.kv']]
        self.root_kv_file = os.path.join(self.appdir,'views','root.kv')

    def get_widget(self,id):
        return self.root.ids[id]

    def build(self):
        for f in self.kv_files:
            Builder.load_file(f, rulesonly=True)
                    
        root = Builder.load_file(self.root_kv_file)
        return root
    
    def on_track_selection(self,adapter):
        player = self.get_widget('player')
        if not adapter.selection:
            return
        selected = adapter.selection[0]
        
        if hasattr(selected,'model'):
            model = selected.model
        else:
            model = selected.parent.model
            
        #player.source = "D:\\Kivy-w32\\test.mp3" #model.filename
        player.source = model.filename
    
    @property
    def tracks_adapter(self):
        return self.get_widget('playlist').adapter
    
    def on_filter(self,adapter):
        if len(adapter.selection):
            self.tracks_adapter.filter(adapter.selection[0].parent.model)
        else:
            self.tracks_adapter.filter(None)
    
    def on_search(self,textinput, value):
        self.tracks_adapter.search(value)
    
    def on_start(self):
#         self.profile = cProfile.Profile()
#         self.profile.enable()
        self.tracks_adapter.bind(on_selection_change=self.on_track_selection)
        self.get_widget('artists').adapter.bind(on_selection_change=self.on_filter)
        self.get_widget('lyricists').adapter.bind(on_selection_change=self.on_filter)
        self.get_widget('composers').adapter.bind(on_selection_change=self.on_filter)
        self.get_widget('generes').adapter.bind(on_selection_change=self.on_filter)
        self.get_widget('search').bind(text=self.on_search)
        

#     def on_stop(self):
#         self.profile.disable()
#         self.profile.dump_stats('myapp.profile')        
        
        