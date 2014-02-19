# -*- coding: utf-8 -*-
'''
Created on:    Feb 2, 2014
@author:        vahid
'''

from kivy.uix.splitter import Splitter
from kivy.properties import OptionProperty
from kivy.uix.carousel import Carousel
from kivy.uix.accordion import AccordionItem
from kivy.factory import Factory

class ArtBox(AccordionItem):
    category = OptionProperty('none',options=['none','artist','composer','lyricist'])
    def __init__(self,*args,**kw):
        super(ArtBox,self).__init__(*args,**kw)
        self.title_template = 'ArtBoxTitle'
    
    def create_carousel(self):
        carousel = Carousel(direction='right')
        for i in range(10):
            src = "http://placehold.it/480x270.png&text=slide-%d&.png" % i
            image = Factory.AsyncImage(source=src, allow_stretch=True)
            carousel.add_widget(image)
        return carousel        
    
    def on_collapse(self,artbox,collapsed):
        super(ArtBox,self).on_collapse(artbox,collapsed)
        if collapsed:
            self.container.clear_widgets()
        else:
            self.container.add_widget(self.create_carousel())


class MediaArt(Splitter):
    def __init__(self,*args,**kw):
        super(MediaArt,self).__init__(*args,**kw)

    @property
    def expanded(self):
        return self.height > self.min_size
    
    def expand(self):
        self.height = self.max_size
        
    
    def on_touch_down(self,touch):
        if self.collide_point(touch.x,touch.y):
            if self._strip.collide_point(touch.x,touch.y) or self.expanded:
                return super(MediaArt,self).on_touch_down(touch)
            else:
                self.expand()
                return True

        