# -*- coding: utf-8 -*-
'''
Created on:    Dec 29, 2013
@author:        vahid
'''

import os
import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# reading pymlconf version (same way sqlalchemy does)
with open(os.path.join(os.path.dirname(__file__), 'chakameh', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)

dependencies = ['pyyaml>=3.10',
                'elixir>=0.7.1']

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="chakameh",
    version=package_version,
    author="Vahid Mardani",
    author_email="vahid.mardani@gmail.com",
    url="http://github.com/pylover/chakameh",
    description="Python music player",
    maintainer="Vahid Mardani",
    maintainer_email="vahid.mardani@gmail.com",
    packages=["chakameh"],
    platforms=["any"],
    long_description=read('README.md'),
    install_requires=dependencies,
    scripts=[
        'bin/csvtotsv',
        'bin/sqlitetocsv',
        'bin/purify-persian',
    ],
    entry_points={
        'console_scripts':[
            "chakameh.import-tracks = chakameh.tools.import_tracks:main",
            "chakameh.find-files = chakameh.tools.find_files:main"]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: Freeware",
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries'
    ],
#    test_suite='pymlconf.tests',
)
