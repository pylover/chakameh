# -*- coding: utf-8 -*-
'''
Created on:    Feb 7, 2014
@author:        vahid
'''

from kivy.uix.gridlayout import GridLayout
# needed to create Fbo, must be resolved in future kivy version
from kivy.core.window import Window

from kivy.graphics import Color, Rectangle, Canvas
from kivy.graphics.fbo import Fbo
from kivy.properties import ObjectProperty
 

class FboGridLayout(GridLayout):
    
    texture = ObjectProperty(None, allownone=True)
 
    def __init__(self, **kwargs):
        self.canvas = Canvas()
        with self.canvas:
            self.fbo = Fbo(size=self.size)
            Color(1, 1, 1)
            self.fbo_rect = Rectangle()
 
        # wait that all the instructions are in the canvas to set texture
        self.texture = self.fbo.texture
        super(FboGridLayout, self).__init__(**kwargs)
 
    def run_fbo(self,lmbda):
        # trick to attach graphics instructino to fbo instead of canvas
        canvas = self.canvas
        try:
            self.canvas = self.fbo
            return lmbda()
        finally:
            self.canvas = canvas
         
 
    def add_widget(self, *largs):
        return self.run_fbo(lambda : super(FboGridLayout, self).add_widget(*largs))
 
    def remove_widget(self, *largs):
        return self.run_fbo(lambda : super(FboGridLayout, self).remove_widget(*largs))
 
    def on_size(self, instance, value):
        self.fbo.size = value
        self.texture = self.fbo.texture
        self.fbo_rect.size = value
 
    def on_pos(self, instance, value):
        self.fbo_rect.pos = value
 
    def on_texture(self, instance, value):
        self.fbo_rect.texture = value
