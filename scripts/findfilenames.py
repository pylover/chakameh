#! /usr/bin/env python

from chakameh.repository import Track


def scan(directory):
    for track in Track.query:
        yield track




if __name__ == '__main__':
    for t in scan():
        print t