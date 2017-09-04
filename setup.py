import sys
from setuptools import setup, find_packages
from os import path
from os import name


CURR_PATH = path.abspath(path.dirname(__file__))
sys.path.append(path.join(CURR_PATH, 'qalab'))

setup(name='qalaboratory',
      version='0.0.5',
      packages=find_packages(exclude=['tests']),
      description = 'QALAB, proyect manager for QA open source proyects',
      author = 'Netzulo Open Source',
      author_email = 'netzuleando@gmail.com',
      url = 'https://github.com/netzulo/qalab',
      download_url = 'https://github.com/netzulo/qalab/tarball/v0.0.5',
      keywords = ['testing', 'logging', 'functional','selenium', 'test', 'installer', 'hub', 'node'],
      install_requires=['appdirs','packaging==16.8','pyparsing','six==1.10.0',
      'nose==1.3.7','nose-testconfig==0.10', 'wget'],
      scripts=['qalab/qalab.py']
     )
