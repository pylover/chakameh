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
        'arts':{
            'noimage': 'stuff/images/noimage.png',
            'directory': '/media/vahid/data/Javdaneha-Arts',
            'extensions': ['png','jpg']
        }
    },
    files=config_filename
)
