# -*- coding: utf-8 -*-
'''
Created on:    Feb 2, 2014
@author:        vahid
'''

from kivy.uix.splitter import Splitter
from kivy.properties import OptionProperty,NumericProperty,ObjectProperty,BooleanProperty
from kivy.uix.carousel import Carousel
from kivy.uix.accordion import AccordionItem
from kivy.factory import Factory
from chakameh.models import Track
from kivy.clock import Clock
from chakameh.config import config


class ArtCarousel(Carousel):
    auto_slide = BooleanProperty(None)
    def __init__(self,*args,**kw):
        super(ArtCarousel,self).__init__(*args,**kw)

    def _do_slide(self,dt):
        self.load_next()
        
    def on_auto_slide(self,*args):
        if self.auto_slide:
            Clock.schedule_interval(self._do_slide, config.arts.slide_interval)
        else:
            Clock.unschedule(self._do_slide)

class ArtBox(AccordionItem):
    category = OptionProperty('none',options=['none','artist','composer','lyricist'])
    model = ObjectProperty()
    
    def __init__(self,*args,**kw):
        super(ArtBox,self).__init__(*args,**kw)
        self.carousel = carousel = ArtCarousel(direction='right',loop=True)
        self.add_widget(carousel)
        if not self.model:
            return
        for filename in self.model.get_arts():
            image = Factory.AsyncImage(source=filename, allow_stretch=True)
            carousel.add_widget(image)

    def on_collapse(self,*args):
        super(ArtBox,self).on_collapse(*args)
        self.carousel.auto_slide = not self.collapse

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
            
            self._container.clear_widgets()
            if track.lyricist:
                self._container.add_widget(ArtBox(category='lyricist',model=track.lyricist,title='شاعر'))
            if track.composer:
                self._container.add_widget(ArtBox(category='composer',model=track.composer,title='آهنگساز'))
            if track.artist:
                self._container.add_widget(ArtBox(category='artist',model=track.artist,title='خواننده'))
        except:
            raise

    def on_touch_down(self,touch):
        if self.collide_point(touch.x,touch.y):
            if self._strip.collide_point(touch.x,touch.y) or self.expanded:
                return super(MediaArt,self).on_touch_down(touch)
            else:
                self.expand()
                return True

