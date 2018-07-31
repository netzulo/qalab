# -*- coding: utf-8 -*-
"""TODO: doc module"""


from os import path
import sys
from setuptools import setup, find_packages


VERSION = '0.1.8'
CURR_PATH = path.abspath(path.dirname(__file__))
# make works script on windows
sys.path.append(path.join(CURR_PATH, 'qalab'))


def readme():
    """Read file on rootpath, README.rst"""
    with open('README.rst') as fil:
        return fil.read()


setup(name='qalaboratory',
      version=VERSION,
      packages=find_packages(exclude=['tests']),
      description=("QALAB, proyect manager for QA open source proyects, "
                   "managing selenium, appium, selendroid drivers"),
      long_description=readme(),
      author='Netzulo Open Source',
      author_email='netzuleando@gmail.com',
      url='https://github.com/netzulo/qalab',
      download_url='https://github.com/netzulo/qalab/tarball/v{}'.format(
          VERSION),
      install_requires=[
          'appdirs',
          'packaging==16.8',
          'pyparsing',
          'six==1.10.0',
          'nose==1.3.7',
          'nose-testconfig==0.10',
          'wget',
          'pytest'
      ],
      setup_requires=[
        'pytest-runner',
        'tox',
      ],
      tests_require=[
        'pytest-html',
        'pytest-dependency',
        'pytest-cov',
      ],
      scripts=['qalab/qaenv.py'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
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
          'edge',
          'appium',
          'mobile',
          'selendroid',
          'automation',
          'pytest'
      ])
