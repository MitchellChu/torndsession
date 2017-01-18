#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 Mitchell Chu

import io

import torndsession

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as des_f:
            buf.append(des_f.read())
    return sep.join(buf)

version = torndsession.version
long_description = read("README.rst")

setup(
    name='torndsession',
    version=version,
    description="Session extensions for Tornado",
    long_description=long_description,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP :: Session',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords='torndsession tornado session redis memcached memory file python',
    author="MitchellChu",
    author_email="zxdjsj@126.com",
    url="http://github.com/mitchellchu/torndsession",
    license="MIT",
    packages=["torndsession"],
    include_package_data=True,
    zip_safe=True,
    install_requires=['tornado',],
)
