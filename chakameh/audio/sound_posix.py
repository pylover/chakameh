# -*- coding: utf-8 -*-
'''
Created on:    Jan 23, 2014
@author:        vahid
'''
from kivy.core.audio import SoundLoader

class Sound(object):
    def __init__(self,filename):
        self.sound = SoundLoader.load(filename)
        if self.sound == None:
            raise Exception('cannot find loader for : %s' % filename)
        self.filename = filename

    def play(self):
        self.sound.play()
         
    def pause(self):
        self.sound.pause()
         
    def unpause(self):
        self.sound.play()
                     
    def stop(self):
        self.sound.stop()
         
    @property
    def length(self):
        if self.sound:
            return self.sound.get_length()
        return 0
    
    def _get_position(self):
        if self.sound:
            return self.sound.get_pos()
        return 0

    def _set_position(self,value):
        if self.sound:
            self.sound.seek(value)

    position = property(_get_position,_set_position)

    def _get_volume(self):
        if self.sound:
            return self.sound.volume * 100
        return 0

    def _set_volume(self,value):
        if self.sound:
            self.sound.volume = value

    
    volume = property(_get_volume,_set_volume)

