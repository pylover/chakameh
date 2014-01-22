# -*- coding: utf-8 -*-
'''
Created on:    Jan 16, 2014
@author:        vahid
'''
from kivy.graphics import Rectangle,Line
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import NumericProperty,StringProperty,ObjectProperty
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.clock import Clock 
from sound import Sound
import os.path

class States(object):
    DEACTIVATED = 0
    STOPPED = 1
    PLAYING = 2
    PAUSED = 3

class PlayButton(ToggleButton):
    padding=NumericProperty(5)
    def __init__(self, **kwargs):
        super(PlayButton,self).__init__(**kwargs)
        self.bind(size=self.on_resize,pos=self.on_resize)
        
    def on_press(self):
        if self.parent:
            self.parent.play_pause()
            
    def on_parent(self,s,p):
        self.parent.bind(player_state=self.on_player_state)
        
    def paint(self):
        with self.canvas:
            self.canvas.clear()
            #Line(rectangle=(self.x,self.y,self.width , self.height))
            offset= self.padding
            if self.parent.player_state == States.PLAYING:
                w = (self.width - offset * 3) /2
                Rectangle(pos=[self.x + offset,self.y+ offset],size=[w, self.height-offset])
                Rectangle(pos=[self.x + offset*2 + w,self.y+offset],size=[w, self.height-offset])
            else:
                Line(width= 2,close= True,
                  joint= "round",cap= "round",
                  points= [self.x+offset,self.top-offset, self.right-offset,self.y + self.height / 2.0, self.x+offset, self.y+offset])            
        
            
    def on_player_state(self,sender,new_state):
        self.paint()
                
    def on_resize(self,s,e):
        self.paint()
        
class PrevButton(Button):
    padding=NumericProperty(5)
    def __init__(self, **kwargs):
        super(PrevButton,self).__init__(**kwargs)        

class NextButton(Button):
    padding=NumericProperty(5)
    def __init__(self, **kwargs):
        Button.__init__(self,**kwargs)        


class AudioPlayer(StackLayout):
    player_state = NumericProperty(States.DEACTIVATED)
    source = StringProperty(None)
    sound = ObjectProperty(None)
    position = NumericProperty(0)
    def __init__(self, **kwargs):
        self.bind(player_state=self.on_player_state,
                  size=self.on_resize,
                  pos=self.on_resize,
                  source=self.on_source)
        
        super(AudioPlayer, self).__init__(**kwargs)
    
    def on_resize(self,*args):
        pass
    
    def on_source(self,*args):
        if self.source.strip() != '' and os.path.exists(self.source):
            self.player_state = States.STOPPED
            self.sound = Sound(self.source)
        else:
            self.player_state = States.DEACTIVATED
    
    def on_player_state(self,sender,new_state):
        pass
    
    def update_position(self,e):
        pass
        #self.position = self.sound.position * 100 / self.sound.length
        
    def play_pause(self):
        if self.player_state == States.DEACTIVATED:
            return
        elif self.player_state == States.PLAYING and self.sound:
            self.sound.pause()
            self.player_state = States.PAUSED            
        elif self.player_state == States.PAUSED:
            self.sound.unpause()
            self.player_state = States.PLAYING
        elif self.player_state == States.STOPPED:
            self.sound.play()
            Clock.schedule_interval(self.update_position,1)
            self.player_state = States.PLAYING

