# -*- coding: utf-8 -*-
'''
Created on:    Jan 24, 2014
@author:        vahid
'''
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListView,SelectableView
from chakameh.uix.adapters import TrackAdapter
from chakameh.uix.loading import Loading

class Playlist(ListView):
    def __init__(self,**kw):
        self._progress= None
        if not 'adapter' in kw:
            kw['adapter'] = TrackAdapter(template='DetailedListItem',
                                         selection_mode='single',
                                         propagate_selection_to_data=False,
                                         )

        super(Playlist,self).__init__(**kw)
    
    def _show_progress(self):
        if self._progress:
            return
        self._progress = Loading()
        self._progress.value = 0
        self.root.add_widget(self._progress)

    def _hide_progress(self):
        if self._progress:
            self.root.remove_widget(self._progress)
            self._progress = None    
#         self._show_progress()
#         Clock.schedule_once(lambda dt: self._hide_progress(),4)    
    
class PlaylistRow(SelectableView,BoxLayout):
    model = ObjectProperty(None)