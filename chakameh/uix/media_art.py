# -*- coding: utf-8 -*-
'''
Created on:    Feb 2, 2014
@author:        vahid
'''

from kivy.uix.splitter import Splitter
from kivy.properties import OptionProperty,NumericProperty,ObjectProperty
from kivy.uix.carousel import Carousel
from kivy.uix.accordion import AccordionItem
from kivy.factory import Factory
from chakameh.models import Track


class ArtCarousel(Carousel):
    def __init__(self,*args,**kw):
        super(ArtCarousel,self).__init__(*args,**kw)

class ArtBox(AccordionItem):
    category = OptionProperty('none',options=['none','artist','composer','lyricist'])
    model = ObjectProperty()
    
    def __init__(self,*args,**kw):
        super(ArtBox,self).__init__(*args,**kw)
#        self.title_template = 'ArtBoxTitle'
        carousel = ArtCarousel(direction='right')
        self.add_widget(carousel)
        if not self.model:
            return
        for filename in self.model.get_arts():
            image = Factory.AsyncImage(source=filename, allow_stretch=True)
            carousel.add_widget(image)
        
    def on_model(self,*args):
        pass    

class MediaArt(Splitter):
    trackid = NumericProperty()
    def __init__(self,*args,**kw):
        super(MediaArt,self).__init__(*args,**kw)

    @property
    def expanded(self):
        return self.height > self.min_size
    
    def expand(self):
        self.height = self.max_size

    def on_trackid(self,*args):
        try:
            track = Track.get(self.trackid)
            print(track)
            self._container.clear_widgets()
            if track.artist:
                self._container.add_widget(ArtBox(category='artist',model=track.artist,title='خواننده'))
            if track.composer:
                self._container.add_widget(ArtBox(category='composer',model=track.composer,title='آهنگساز'))
            if track.lyricist:
                self._container.add_widget(ArtBox(category='lyricist',model=track.lyricist,title='نوازنده'))
        except:
            raise

    def on_touch_down(self,touch):
        if self.collide_point(touch.x,touch.y):
            if self._strip.collide_point(touch.x,touch.y) or self.expanded:
                return super(MediaArt,self).on_touch_down(touch)
            else:
                self.expand()
                return True

