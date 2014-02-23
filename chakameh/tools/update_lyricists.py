#! /usr/bin/env python

from __future__ import print_function

import argparse
import sys
import csv


parser = argparse.ArgumentParser(description='Find and store media filenames.')
parser.add_argument('inputfile', metavar='PATH',nargs='?',help='CSV file to update artist from it.')
parser.add_argument('-c','--config-file', metavar='CONFIGFILE',help='Chakameh config file.')
args = parser.parse_args()

from chakameh.config import config
if args.config_file:
    config.load_files(args.config_file)

sys.argv = sys.argv[:1]

from chakameh.models import Lyricist, session

def read(file):
    reader = csv.reader(file,delimiter='\t',dialect='excel')
    for row in reader:
        _id, title, realname = row[:3]
        yield _id, title.decode('utf8'), realname.decode('utf8'), row[3:]
        

    
def main():
    if args.inputfile:
        file = open(args.inputfile)
    else:
        file = sys.stdin

    try:
        for _id, title, realname, tags in read(file):
            print(_id, title, realname, tags)
            artist = Lyricist.query.filter(Lyricist.title == title.strip()).first()
            artist.realname = realname
            artist.tags = ','.join(tags)
            session.commit()
    finally:
        if file != sys.stdin:
            file.close()
    return 0
    
if __name__ == '__main__':
    sys.exit(main())