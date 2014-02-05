# -*- coding: utf-8 -*-
'''
Created on:    Jan 24, 2014
@author:        vahid
'''
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListView,SelectableView
from chakameh.uix.adapters import TrackAdapter

class Playlist(ListView):
    def __init__(self,**kw):
        if not 'adapter' in kw:
            kw['adapter'] = TrackAdapter(template='DetailedListItem',
                                         selection_mode='single',
                                         propagate_selection_to_data=False,
                                         )

        super(Playlist,self).__init__(**kw)
    
class PlaylistRow(SelectableView,BoxLayout):
    model = ObjectProperty(None)