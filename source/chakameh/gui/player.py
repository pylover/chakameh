# -*- coding: utf-8 -*-
'''
Created on:    Jan 16, 2014
@author:        vahid
'''
from kivy.properties import NumericProperty,StringProperty,ObjectProperty
from kivy.uix.button import Button
from kivy.clock import Clock 
from sound import Sound
import os.path
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

class States(object):
    DEACTIVATED = 0
    STOPPED = 1
    PLAYING = 2
    PAUSED = 3

class PlayButton(Image):
    player = ObjectProperty()
#     def __init__(self, **kwargs):
#         super(PlayButton,self).__init__(**kwargs)
#         self.bind(size=self.on_resize,pos=self.on_resize)
        
    def on_touch_down(self, touch):
        '''.. versionchanged:: 1.4.0'''
        if self.collide_point(*touch.pos):
            self.parent.play_pause()
            return True
         
#     def on_parent(self,s,p):
#         self.parent.bind(player_state=self.on_player_state)
#          
#     def on_player_state(self,sender,new_state):
#         self.paint()
#         
#     def paint(self):
#         with self.canvas:
#             self.canvas.clear()
#             #Line(rectangle=(self.x,self.y,self.width , self.height))
#              
#             if self.parent.player_state == States.PLAYING:
#                 w = (self.width - self.padding * 3) /2
#                 Rectangle(pos=[self.x + self.padding,self.y+ self.padding],size=[w, self.height-self.padding*2])
#                 Rectangle(pos=[self.x + self.padding*2 + w,self.y+self.padding],size=[w, self.height-self.padding*2])
#             else:
#                 Line(width= 2,close= True,
#                   joint= "round",cap= "round",
#                   points= [self.x+self.padding,self.top-self.padding, self.right-self.padding,self.y + self.height / 2.0, self.x+self.padding, self.y+self.padding])            
#          
#              
#                  
#     def on_resize(self,s,e):
#         self.paint()
        
class PrevButton(Button):
    padding=NumericProperty(5)
    def __init__(self, **kwargs):
        super(PrevButton,self).__init__(**kwargs)        

class NextButton(Button):
    padding=NumericProperty(5)
    def __init__(self, **kwargs):
        Button.__init__(self,**kwargs)        


class AudioPlayer(BoxLayout):
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
    
    def set_position(self,value):
        if abs( self.position - value)>1:
            self.sound.position = value * self.sound.length / 100.0
    
    
    def update_position(self,e):
        self.position = self.sound.position * 100.0 / self.sound.length
        
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
            Clock.schedule_interval(self.update_position,.2)
            self.player_state = States.PLAYING

