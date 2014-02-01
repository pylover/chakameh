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
            return self.sound.get_length() * 1000
        return 0
    
    def _get_position(self):
        if self.sound:
            return self.sound.get_pos() * 1000
        return 0

    def _set_position(self,value):
        if self.sound:
            self.sound.seek(value) / 1000.0

    position = property(_get_position,_set_position)

