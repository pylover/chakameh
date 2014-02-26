# -*- coding: utf-8 -*-
'''
Created on:    Jan 27, 2014
@author:        vahid
'''

from kivy.app import App
from kivy.lang import Builder
from chakameh.models import ApplicationInfo,session
from datetime import datetime
import os.path
import cProfile

class ChakamehApp(App):
    
    def __init__(self):
        App.__init__(self)
        self.appdir = os.path.abspath(os.path.dirname(__file__))
        ApplicationInfo.single().last_run = datetime.now()
        session.commit()
        
        self.kv_files = [os.path.join(self.appdir,'views',f) for f in ['global.kv',
                                                                       'player.kv',
                                                                       'rightpane.kv',
                                                                       'playlist.kv',
                                                                       'mediaart.kv',
                                                                       'loading.kv']]
        self.root_kv_file = os.path.join(self.appdir,'views','root.kv')

    def join_root(self,p):
        return os.path.join(self.appdir,'..',p)

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
        
        if not selected.parent or not selected.parent.filename:
            return 
            
        filename = selected.parent.filename
        trackid = selected.parent.objid
        
        if player.source == filename:
            player.source = filename
            prop = player.property('source') 
            prop.dispatch(player.__self__)
        else:
            player.source = filename
        
        self.get_widget('mediaart').trackid = trackid
        
    
    @property
    def tracks_adapter(self):
        return self.get_widget('playlist').adapter
    
    def on_filter(self,adapter):
        if len(adapter.selection):
            s = adapter.selection[0].parent
            self.tracks_adapter.filter(s.entity_name,s.objid)
        else:
            self.tracks_adapter.filter(None)
    
    def on_search(self,textinput, value):
        self.tracks_adapter.search(value)
    
    def on_track_end(self,player):
        pl = self.get_widget('playlist')
        pl.adapter.select_next_track()

    def on_track_start(self,player):
        pass
        
        
    
    def on_start(self):
        #self.profile = cProfile.Profile()
        #self.profile.enable()
        self.tracks_adapter.bind(on_selection_change=self.on_track_selection)
        self.get_widget('player').bind(on_track_end=self.on_track_end,
                                       on_track_start=self.on_track_start)
        
        self.get_widget('rightpane').ids['artists'].adapter.bind(on_selection_change=self.on_filter)
        self.get_widget('rightpane').ids['lyricists'].adapter.bind(on_selection_change=self.on_filter)
        self.get_widget('rightpane').ids['composers'].adapter.bind(on_selection_change=self.on_filter)
        self.get_widget('rightpane').ids['generes'].adapter.bind(on_selection_change=self.on_filter)
        self.get_widget('rightpane').ids['search'].bind(text=self.on_search)

    def on_stop(self):
        #self.profile.disable()
        #self.profile.dump_stats('myapp.profile')
        pass
        
        