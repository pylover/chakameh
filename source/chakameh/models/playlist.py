# -*- coding: utf-8 -*-
'''
Created on:    Jan 17, 2014
@author:        vahid
'''

from elixir import Entity,metadata,Field,Unicode,Integer,UnicodeText,session,setup_all,Binary

from reader import AudioFile

metadata.bind = "sqlite:///../../data/tracks.sqlite"
metadata.bind.echo = False


class Playlist(list):
    pass
