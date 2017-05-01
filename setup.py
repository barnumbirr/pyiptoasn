#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='pyiptoasn',
    version='0.1',
    url='https://github.com/mrsmn/pyiptoasn',
    download_url='https://github.com/mrsmn/pyiptoasn/archive/master.zip',
    author='Martin Simon',
    author_email='me@martinsimon.me',
    license='Apache v2.0 License',
    packages=['pyiptoasn'],
    description='A python wrapper around iptoasn.com',
    long_description=open('README.md','r').read(),
    keywords=['iptoasn', 'ASN', 'IP', 'wrapper'],
)
