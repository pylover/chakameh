#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function 
import sys
import argparse
import re

parser = argparse.ArgumentParser(description='Find and store media filenames.')
parser.add_argument('inputfile',metavar='FILENAME', nargs='?',help='Tracks tsv file.')
parser.add_argument('-c','--config-file', metavar='CONFIGFILE',help='Chakameh config file.')
args = parser.parse_args()

from chakameh.config import config
if args.config_file:
    config.load_files(args.config_file)
 
sys.argv = sys.argv[:1]


from chakameh.models import Artist,Composer,Genere,Lyricist,Track,Category

def read():
    if args.inputfile:
        reader = open(args.inputfile)
    else:
        reader = sys.stdin
        
    l = 0
    try:
        for line in reader.readlines():
            columns = [c.strip() for c in line.decode('utf8').split('\t')]
            l+=1
            yield columns
            
    except:
        print('LINE: %s' % l , end='\n', file=sys.stderr)
        raise
    finally:
        if reader != sys.stdin:
            reader.close()
        
class LineTypes(object):
    UNKNOWN = 0
    CATEGORY= 1
    MEDIA_NO = 2
    DATA = 3
    HEADER = 4

def parse():
    #print(set([len(l) for l in read()]))
    counter=0
    linetype = LineTypes.UNKNOWN
    counts = [] 
 
    for l in read():
        counter +=1
        columns_count = len(l)
        counts.append(columns_count)
        
        if columns_count > 1:
            if re.match('\d{1,6}[-\d{1,4}]{0,1}',l[0]):
                # DataRow
                linetype = LineTypes.DATA
                #print('DATA:%d: %s' % (counter, '\t'.join(l).encode('utf8').replace('\t',' | ')))
            elif l[0].startswith(u'\u0634\u0645\u0627\u0631\u0647'):
                #HEADER
                #print(('HEADER:%d: %s' % (counter, l[0].encode('utf8'))))
                linetype = LineTypes.HEADER
            elif re.match('^CD',l[0]):
                linetype = LineTypes.MEDIA_NO
                #print(('MEDIA_NO:%d: %s' % (counter, l[0].encode('utf8'))))
            else:
                linetype = LineTypes.CATEGORY
                #print(('CATEGORY:%d: %s' % (counter, l[0].encode('utf8'))))
        
        else:
            #print(('UNKNOWN:%d :%s' % (counter, l[0].encode('utf8'))))
            linetype = LineTypes.UNKNOWN
        yield linetype, l
            
def start():
    
    id = None
    category = None
    mediano = None
    artist = None
    prime = None
    composer = None
    lyricist = None
    dastgah = None
    
    for linetype,line in parse():
        if linetype == LineTypes.CATEGORY:
            category =  Category.ensure(line[0])
        elif linetype == LineTypes.MEDIA_NO:
            mediano = re.match('^CD\s(?P<NO>\d{1,2})\s', line[0]).groups()[0]
        elif linetype == LineTypes.DATA:
            code = line[0]
            prime = line[1]
            title = line[2]
            artist = Artist.ensure(line[3],line[4]) # artist, realname            
            composer = Composer.ensure(line[5])
            lyricist = Lyricist.ensure(line[6])
            dastgah = Genere.ensure(line[7])
            comment = line[8]
            language = line[9]
            
            track = Track.ensure(code, prime,
                           title = title,
                           artist = artist,
                           composer = composer,
                           lyricist = lyricist,
                           genere = dastgah,
                           mediano = mediano,
                           comment = comment,
                           language = language)
            
            print('\t'.join([ str(track.id),
                              code,
                              mediano,
                              prime]))

#                               unicode(category),
#                               prime,
#                               unicode(artist),
#                               unicode(composer),
#                               unicode(lyricist),
#                               unicode(dastgah)]).encode('utf8'))
    
def main():
    start()
    return 0

if __name__ == '__main__':
    sys.exit(main())