# -*- coding: utf-8 -*-
'''
Created on Jan 16, 2014

@author: vahid
'''

from chakameh.main import start
import os.path

thisdir = os.path.dirname(__file__)


if __name__ == '__main__':
    start(config_filename=os.path.join(thisdir,'development.conf'))
    