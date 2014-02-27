# -*- coding: utf-8 -*-
'''
Created on:    Feb 28, 2014
@author:        vahid
'''
import csv


def read(file):
    reader = csv.reader(file,delimiter='\t',dialect='excel')
    for row in reader:
        _id, title, realname = row[:3]
        yield _id, title.decode('utf8'), realname.decode('utf8'), row[3:]