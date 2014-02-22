# -*- coding: utf-8 -*-
'''
Created on:    Jan 16, 2014
@author:        vahid
'''
import os.path
from kivy.properties import NumericProperty,StringProperty,ObjectProperty
from kivy.uix.button import Button
from kivy.clock import Clock 
from chakameh.audio import Sound
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from chakameh.config import config

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
    total_time = StringProperty(0)
    current_time = StringProperty(0)
    volume = NumericProperty(0)
    
    def __init__(self, **kwargs):
        self.bind(player_state=self.on_player_state,
                  size=self.on_resize,
                  pos=self.on_resize,
                  source=self.on_source)
        self.register_event_type('on_track_start')
        self.register_event_type('on_track_end')
        super(AudioPlayer, self).__init__(**kwargs)
    
    def on_resize(self,*args):
        pass
    
    def on_source(self,*args): 
        filename = os.path.join(config.media_root,self.source)
        #print filename
        if os.path.exists(filename):
            self.player_state = States.STOPPED
            self.stop()
            self.sound = Sound(filename)
            if not self.sound:
                pass#TODO: raise exception or not for fail safe app development
            self.play_pause()
        else:
            self.player_state = States.DEACTIVATED
    
    def on_player_state(self,sender,new_state):
        pass
    
    def get_readable_time(self,total_seconds):
        minutes = total_seconds / 60.0
        seconds = total_seconds % 60.0
        return '%.2d:%.2d' % (minutes, seconds) 
        
    
    def set_position(self,value):
        if not self.sound:
            return
        if abs( self.position - value)>1:
            self.sound.position = value * self.sound.length / 100.0

    def set_volume(self,value):
        if not self.sound:
            return
        self.sound.volume = value
    
    def update_position(self,e):
        if self.sound.length > 0:
            self.total_time = self.get_readable_time(self.sound.length)
            self.current_time = self.get_readable_time(self.sound.position)
            self.position = self.sound.position * 100.0 / self.sound.length
            self.volume = self.sound.volume
            if abs(self.sound.position - self.sound.length) < 100:
                self.dispatch('on_track_end')
        
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
            self.dispatch('on_track_start')
            self.sound.play()
            Clock.schedule_interval(self.update_position,.3)
            self.player_state = States.PLAYING

    def on_track_end(self,*args,**kw):
        pass

    def on_track_start(self,*args,**kw):
        pass
