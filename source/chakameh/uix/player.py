# -*- coding: utf-8 -*-
'''
Created on:    Jan 16, 2014
@author:        vahid
'''
import os.path
from kivy.properties import NumericProperty,StringProperty,ObjectProperty
from kivy.uix.button import Button
from kivy.clock import Clock 
from chakameh.audio.sound import Sound
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

class States(object):
    DEACTIVATED = 0
    STOPPED = 1
    PLAYING = 2
    PAUSED = 3

class PlayButton(Image):
    player = ObjectProperty()
        
    def on_touch_down(self, touch):
        '''.. versionchanged:: 1.4.0'''
        if self.collide_point(*touch.pos):
            self.parent.play_pause()
            return True
        
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
            self.stop()
            self.sound = Sound(self.source)
            self.play_pause()
        else:
            self.player_state = States.DEACTIVATED
    
    def on_player_state(self,sender,new_state):
        pass
    
    def set_position(self,value):
        if abs( self.position - value)>1:
            self.sound.position = value * self.sound.length / 100.0
    
    
    def update_position(self,e):
        if self.sound.length > 0:
            self.position = self.sound.position * 100.0 / self.sound.length
        
    def stop(self):
        if self.sound:
            self.sound.stop()
        self.player_state = States.STOPPED
        
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

