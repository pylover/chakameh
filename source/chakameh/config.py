'''
Created on Jan 26, 2013

@author: vahid
'''

from pymlconf import ConfigManager
import os
thisdir = os.path.dirname(__file__)
config_filename=os.path.join(thisdir,'../development.conf')

config = ConfigManager(
    init_value={
        'data_uri': 'sqlite:///../data/db.sqlite',
        'media_root':       '/media/vahid/data/Javdaneha',
        'media_arts_root':  '/media/vahid/data/Javdaneha-Arts',
        'media_arts_extensions':    ['png']
    },
    files=config_filename
)
