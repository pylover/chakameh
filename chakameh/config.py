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
        'arts':{
            'noimage': 'stuff/images/noimage.png',
            'root': '/media/vahid/data/Javdaneha-Arts',
            'extensions': ['png','jpg']
        }
    },
)
