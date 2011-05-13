#!/usr/bin/python
# -*- coding: utf-8 -*-

# django-bipipe
# https://github.com/orygens/django-bigpipe

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 Orygens contato@orygens.com

from setuptools import setup, find_packages
from django_bigpipe import __version__

setup(
    name = 'django-bigpipe',
    version = '.'.join([str(item) for item in __version__]),
    description = "django-bigpipe are a jquery-bigpipe extension to django web framework.",
    long_description = """
django-bigpipe are a jquery-bigpipe (https://github.com/orygens/jquery-bigpipe) extension to django web framework.
""",
    keywords = 'django web',
    author = u'Orygens',
    author_email = 'contato@orygens.com',
    url = 'https://github.com/orygens/django-bigpipe',
    license = 'MIT',
    classifiers = ['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: MacOS',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.6'
    ],
    packages = find_packages(),
    package_dir = {"django_bigpipe": "django_bigpipe"},
    include_package_data = True,

    install_requires=[
        "django"
    ],

)
