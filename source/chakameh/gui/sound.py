# -*- coding: utf-8 -*-
'''
Created on:    Jan 23, 2014
@author:        vahid
'''
import pygame
pygame.init()
from pygame.mixer import music

class Sound(object):
    def __init__(self,filename):
        self.filename = filename
        music.load(filename)
    
    def play(self):
        music.play()
        
    def pause(self):
        music.pause()
        
    def unpause(self):
        music.unpause()
        
    def stop(self):
        music.stop()
        
    @property
    def position(self):
        return music.get_pos()
