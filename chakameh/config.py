'''
Created on Jan 26, 2013

@author: vahid
'''

from pymlconf import ConfigManager
import os
thisdir = os.path.dirname(__file__)


config = ConfigManager(
    init_value={
        'data_uri': '',
        'media_root':       '',
        'background_image': os.path.join(thisdir,'stuff/images/back.png'),
        'arts':{
            'noimage': 'stuff/images/noimage.png',
            'root': '/media/vahid/data/Javdaneha-Arts',
            'extensions': ['png','jpg'],
            'slide_interval': 30
        }
    },
)
