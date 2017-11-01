# -*- coding: utf-8 -*-
"""TODO: doc module"""


from os import path
import sys
from setuptools import setup, find_packages


CURR_PATH = path.abspath(path.dirname(__file__))
# make works script on windows
sys.path.append(path.join(CURR_PATH, 'qalab'))


def readme():
    """Read file on rootpath, README.rst"""
    with open('README.rst') as fil:
        return fil.read()


setup(name='qalaboratory',
      version='0.0.7',
      packages=find_packages(exclude=['tests']),
      description='QALAB, proyect manager for QA open source proyects',
      long_description=readme(),
      author='Netzulo Open Source',
      author_email='netzuleando@gmail.com',
      url='https://github.com/netzulo/qalab',
      download_url='https://github.com/netzulo/qalab/tarball/v0.0.7',
      install_requires=[
          'appdirs',
          'packaging==16.8',
          'pyparsing',
          'six==1.10.0',
          'nose==1.3.7',
          'nose-testconfig==0.10',
          'wget'
      ],
      keywords=[
          'testing',
          'logging',
          'functional',
          'selenium',
          'test',
          'installer',
          'hub',
          'node',
          'qa',
          'driver',
          'chrome',
          'firefox',
          'phantomjs',
          'iexplorer',
          'edge'
      ],
      scripts=['qalab/qalab.py']
     )
