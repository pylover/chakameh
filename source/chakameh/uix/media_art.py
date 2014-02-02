# -*- coding: utf-8 -*-
'''
Created on:    Feb 2, 2014
@author:        vahid
'''

from kivy.uix.stacklayout import StackLayout
from kivy.properties import OptionProperty

class MediaArt(StackLayout):
    expand_status = OptionProperty('collapsed',options=['collapsed','expanded'])
    def __init__(self,*args,**kw):
        self.register_event_type('on_expand')
        self.register_event_type('on_collapse')
        super(StackLayout,self).__init__(*args,**kw)
    
    def on_touch_down(self,touch):
        if self.collide_point(touch.x, touch.y):
            self.expand_status = 'collapsed' if self.expand_status == 'expanded' else 'expanded'
            
    
    def on_expand_status(self,*args,**kw):
        if self.expand_status == 'expanded':
            self.dispatch('on_expand')
        else:
            self.dispatch('on_collapse')
    
    def on_expand(self):
        pass
    
    def on_collapse(self):
        pass
            
        