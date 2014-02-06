# -*- coding: utf-8 -*-
'''
Created on:    Feb 5, 2014
@author:        vahid
'''

from kivy.uix.floatlayout import FloatLayout


class Loading(FloatLayout):

    def cancel(self, *largs):
        '''Cancel any action from the FileChooserController.
        '''
        if self.parent:
            self.parent.cancel()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            super(Loading, self).on_touch_down(touch)
            return True

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            super(Loading, self).on_touch_move(touch)
            return True

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            super(Loading, self).on_touch_up(touch)
            return True


