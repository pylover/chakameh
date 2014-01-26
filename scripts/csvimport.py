#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function 
import sys
from chakameh.repository import Artist,Category,Composer,Genere,Lyricist
import re   

def read():
    #reader = sys.stdin
    reader = open('../docs/tables.tsv')
    l = 0
    try:
        for line in reader.readlines():
            columns = [c.strip() for c in line.decode('utf8').split('\t')]
            l+=1
            yield columns
            
    except:
        print('LINE: %s' % l , *objs, end='\n', file=sys.stderr)
        raise
        
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
            artist = Atist.ensure(line[2])
            composer = Composer.ensure(line[3])
            lyricist = Lyricist.ensure(line[4])
            dastgah = Genere(line[5])
            
            track = Track.ensure(code, prime,
                           artist = artist,
                           composer = composer,
                           lyricist = lyricist,
                           genere = dastgah,
                           mediano = mediano)
            
            print('\t'.join([ str(track.id),
                              code,
                              mediano,
                              str(category),
                              prime,
                              str(artist),
                              str(composer),
                              str(lyricist),
                              str(dastgah)]).encode('utf8'))
    
    #print(set(counts))
if __name__ == '__main__':
    start()