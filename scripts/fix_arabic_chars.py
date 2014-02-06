#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys

class ReplacementList(object):
    def __init__(self):
        self._d = {}
        
    def add(self,key, by=None):
        if by:
            self._d[key] = by
        else:
            raise ValueError
    
    def get_replacement_dict(self):
        return self._d

replacements = ReplacementList()
replacements.add(u'ي', by=u'ی')
replacements = replacements.get_replacement_dict()

def refine_string(data):
    res = data
    for k,v in replacements.items():
        res = res.replace(k,v)
    return res

if __name__ == '__main__':
    reader = sys.stdin
    writer = sys.stdout
    for line in reader.readlines():
        writer.write(refine_string(line.decode('utf8')).encode('utf8'))
    
    sys.exit(0)
    
    
