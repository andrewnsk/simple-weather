#!/usr/bin/env python

from setuptools import setup

setup(
    name='sweather',
    version='0.0.2',
    description='pyowm wrapper',
    author='Andrew Dorokhin (@andrewnsk)',
    author_email='andrew@dorokhin.moscow',
    url='http://github.com/andrewnsk/sweather',
    packages=['sweather', 'tests.unit'],
    long_description="""\
      It's my own temporary testing project
      """,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
    ],
    package_data={
        '': ['*.txt', '*.xsd']
    },
    keywords='weather arduino',
    license='GNU v3',
    test_suite='tests',
    install_requires=[
          'pyowm',
          'mako'
      ]
)
