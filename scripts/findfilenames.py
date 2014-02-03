#! /usr/bin/env python

import os
import re
from chakameh.models import Track, session
from chakameh.config import config

def update_tracks(dir,code):
    pass
    

def scan():
    _proceed = 0
    _found = 0
    _errors = 0
    _max_errors = 10
    _total = Track.query.count()
    for track in Track.query.order_by(Track.code):
        _proceed+= 1
        media_dir = get_media_dir(track.mediano)
        
        splited_code = track.code.split('-')
        if len(splited_code) == 2:
            db_code, db_subcode = splited_code
        else:
            db_code, db_subcode = splited_code[0], '1'         
        db_code, db_subcode = int(db_code), int(db_subcode)
        
        # start searching for the directory which contains the music files 
        for d in os.listdir(media_dir):
            fullpath = os.path.join(media_dir,d)
            if os.path.isdir(fullpath):
                m = re.match('^(?P<code>\d{1,4})\s?-', d)
                if not m:
                    continue
                else:
                    if db_code != int(m.groupdict()['code']):
                        continue
                
                #Directory found, searching for files:
                for f in os.listdir(fullpath):
                    filename = os.path.join(fullpath,f)
                    if os.path.isfile(filename):
                        m = re.match('^\s?(?P<code>\d{1,4})\s*[-_\.]*\s*(?P<subcode>\d{1,4})?', f)
                        if not m:
                            continue
                        else:
                            code , subcode = int(m.groupdict()['code']), int(1 if not m.groupdict()['subcode'] else m.groupdict()['subcode'])
#                             if code == 4:
#                                 iiii = 7
                            if code == db_code and subcode == db_subcode:
                                # Track found exactly
                                new_filename = os.path.abspath(os.path.join(fullpath,f))
                                if track.filename != new_filename:
                                    track.filename = os.path.relpath(new_filename,config.media_root)
                                    session.commit()
                                    _found += 1
                                     #yield 'FOUND', code , subcode
                            else:
                                pass

        persent = _proceed * 100 / _total
        v = _proceed * 20 / _total
        print 'Progress(%s%% == %s/%s errors: %s): %s'% (persent, _found,_proceed,_errors,v * '#') 
                                
                            
#                     tracks = Track.query.filter(Track.code.like('%s%%' % code))
#                     for t in tracks:
#                         yield t

_media_dirs= {}
def get_media_dir(no):
    global _media_dirs
    root = os.path.abspath("/media/vahid/data/Javdaneha")
    
    if len(_media_dirs) <= 0:
        for f in os.listdir(root):
            fullpath = os.path.join(root,f)
            if os.path.isdir(fullpath):
                m = re.match('^(?P<mediano>\d{1,2})-',f)
                if m:
                    _media_dirs[int(m.groupdict()['mediano'])] = fullpath
    return _media_dirs[no]
    
if __name__ == '__main__':
    scan()