# -*- coding: utf-8 -*-
'''
Created on:    Jan 24, 2014
@author:        vahid
'''
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty,OptionProperty,StringProperty
from kivy.uix.listview import ListView,SelectableView
from kivy.uix.button import Button
from chakameh.uix.adapters import TrackAdapter
from chakameh.uix.loading import Loading

class ColumnHeaderCell(Button):
    column = StringProperty()
    sort_status = OptionProperty('none',options=['none','asc','desc'])
    def __init__(self,*args,**kw):
        super(ColumnHeaderCell,self).__init__(*args,**kw)
        
    def on_press(self):
        if self.sort_status == 'none':
            self.sort_status = 'asc'
        elif self.sort_status == 'asc':
            self.sort_status = 'desc'
        else:
            self.sort_status = 'none'

class Playlist(ListView):
    header = ObjectProperty(None)
    def __init__(self,**kw):
        self._progress= None
        if not 'adapter' in kw:
            kw['adapter'] = TrackAdapter(template='DetailedListItem',
                                         selection_mode='single',
                                         propagate_selection_to_data=False)

        super(Playlist,self).__init__(**kw)
    
    def _show_progress(self):
        if self._progress:
            return
        self._progress = Loading()
        self._progress.value = 0
        self.add_widget(self._progress)

    def _hide_progress(self):
        if self._progress:
            self.remove_widget(self._progress)
            self._progress = None    
#         self._show_progress()
#         Clock.schedule_once(lambda dt: self._hide_progress(),4)    
    
#     def populate(self,*args):
#         ctime = datetime.now()
#         super(Playlist,self).populate(*args)
#         print "loaded in: %s seconds" % (datetime.now() - ctime).total_seconds()
    
class PlaylistRow(SelectableView,BoxLayout):
    model = ObjectProperty(None)