# -*- coding: utf-8 -*-
'''
Created on:    Jan 24, 2014
@author:        vahid
'''
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.selectableview import SelectableView

class Playlist(BoxLayout):
    current = ObjectProperty(None)
    
class PlaylistRow(SelectableView,BoxLayout):
    model = ObjectProperty(None)