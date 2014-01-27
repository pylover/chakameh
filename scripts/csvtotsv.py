#!/usr/bin/env python

from __future__ import print_function
import sys

def read(): 
    c,l= 0,0
    try:
        for line in sys.stdin.readlines():
            columns = line.strip()[4:].decode('utf8').split(u',')
            row = []
            l+=1
            for column in columns:
                c+=1
                #if len(column) >= 1 and column <> ('\n'):
                row.append(column.strip())
            yield row
    except:
        print('LINE: %s COLUMN: %s' % (l,c) , end='\n', file=sys.stderr)
        raise
    

def start():
    for l in read():
        print(u'\t'.join(l).encode('utf8'))

        
if __name__ == '__main__':
    start()