# -*- coding: utf-8 -*-
'''
Created on:    Jan 27, 2014
@author:        vahid
'''

from kivy.app import App
# from chakameh.uix.adapters import TrackAdapter
# from kivy.uix.listview import CompositeListItem, ListItemButton, ListItemLabel
#from kivy.clock import Clock
#from kivy.uix.listview import ListView
from kivy.lang import Builder
import os.path

class ChakamehApp(App):
    def __init__(self):
        App.__init__(self)
        self.appdir = os.path.abspath(os.path.dirname(__file__))
        
        self.kv_files = [os.path.join(self.appdir,'views',f) for f in ['global.kv','player.kv','rightpane.kv','playlist.kv']]
        self.root_kv_file = os.path.join(self.appdir,'views','root.kv')

    def build(self):
        for f in self.kv_files:
            Builder.load_file(f, rulesonly=True)
                    
        root = Builder.load_file(self.root_kv_file)
        print root.ids

        return root

#      source: '' if not playlistview.adapter.selection else playlistview.adapter.selection[0].parent.model.filename        
#        self.root.ids['player'].source = 

    def update_tracks(self,dt):
        pass
        #self.root.canvas.ask_update()

    def on_start(self):
        pass
        #Clock.schedule_interval(self.update_tracks,1)
        
        
