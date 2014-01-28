# -*- coding: utf-8 -*-
'''
Created on:    Jan 23, 2014
@author:        vahid
'''
import pygame
pygame.init()

# import time
# import pymedia.audio.acodec as acodec
# import pymedia.audio.sound as sound
# import pymedia.muxer as muxer
# import threading
# 
# class Sound(object):
#     def __init__(self,filename):
#         self.playing = False
#         self.stopped = True
#         self.filename = filename
#         codec_id = acodec.getCodecID(str.split(self.filename , '.' )[ -1 ].lower())
#         self.decoder = acodec.Decoder( {'id': codec_id} )
#     
#     def play(self):
#         self.thread = threading.Thread(target=self._play)
#         self.thread.start()
#         self.stopped = False
#         self.playing = True
#     
#     def _play(self):
#         f= open( self.filename, 'rb' )
#         s= f.read( 8192 )
#         r= self.decoder.decode( s )
#         snd= sound.Output( int(r.sample_rate), r.channels, sound.AFMT_S16_LE, 0 )
#         while len( s )>0:
#             if not self.playing:
#                 time.sleep(.2)
#                 continue
#             if self.stopped:
#                 break
#             if r: snd.play( r.data )
#             s= f.read( 512 )
#             r= self.decoder.decode( s )
# 
#         
#         while snd.isPlaying(): time.sleep( .05 )
#         threading.thread.join()
#         
#     def pause(self):
#         self.playing = False
#         
#     def unpause(self):
#         self.playing = True
#         
#     def stop(self):
#         self.stopped = True
#         
#     @property
#     def position(self):
#         return 0


#from pygame.mixer import music

# class Sound(object):
#     def __init__(self,filename):
#         self.filename = filename
#         music.load(filename)
#     
#     def play(self):
#         music.play()
#         
#     def pause(self):
#         music.pause()
#         
#     def unpause(self):
#         music.unpause()
#         
#     def stop(self):
#         music.stop()
#         
#     @property
#     def position(self):
#         return music.get_pos()

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