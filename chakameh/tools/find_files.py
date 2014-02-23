#! /usr/bin/env python

from __future__ import print_function
import os
import re
import argparse
import sys

parser = argparse.ArgumentParser(description='Find and store media filenames.')
parser.add_argument('path', metavar='PATH',help='Media directory.')
parser.add_argument('-c','--config-file', metavar='CONFIGFILE',help='Chakameh config file.')
args = parser.parse_args()

from chakameh.config import config
if args.config_file:
    config.load_files(args.config_file)
 
sys.argv = sys.argv[:1]

from chakameh.models import Track, session


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
                            if code == db_code and subcode == db_subcode:
                                # Track found exactly
                                new_filename = os.path.abspath(os.path.join(fullpath,f))
                                if track.filename != new_filename:
                                    track.filename = os.path.relpath(new_filename,args.path)
                                    session.commit()
                                    _found += 1
                            else:
                                pass

        persent = _proceed * 100 / _total
        v = _proceed * 20 / _total
        print('Progress(%s%% == %s/%s errors: %s): %s'% (persent, _found,_proceed,_errors,v * '#')) 

_media_dirs= {}
def get_media_dir(no):
    global _media_dirs
    root = os.path.abspath(args.path)
    
    if len(_media_dirs) <= 0:
        for f in os.listdir(root):
            fullpath = os.path.join(root,f)
            if os.path.isdir(fullpath):
                m = re.match('^(?P<mediano>\d{1,2})-',f)
                if m:
                    _media_dirs[int(m.groupdict()['mediano'])] = fullpath
    return _media_dirs[no]
    
def main():
    scan()
    return 0
    
if __name__ == '__main__':
    sys.exit(main())