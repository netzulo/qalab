# QA laboratory 

+ **Linux Deploy**: [![Build Status](https://travis-ci.org/netzulo/qalab.svg?branch=master)](https://travis-ci.org/netzulo/qalab)
+ **Windows Deploy**: [![Build status](https://ci.appveyor.com/api/projects/status/f4orjhi6vjgsxxq9?svg=true)](https://ci.appveyor.com/project/netzulo/qalab-v060g)


## _How to install ?_

+ 1. Clone this repo : `git clone https://github.com/netzulo/qalab.git`
+ 2. Enter on repo directory : `cd qalab`
+ 3. Clone submodules : `git submodule update --init --recursive`
+ 4. Attach branches HEAD: `git submodule foreach git checkout master`

## SubModules

+ 1. [qadoc](https://github.com/netzulo/qadoc)  : [![Build Status](https://travis-ci.org/netzulo/qadoc.svg?branch=master)](https://travis-ci.org/netzulo/qadoc)
+ 2. [qacode](https://github.com/netzulo/qacode) : [![Build Status](https://travis-ci.org/netzulo/qacode.svg?branch=master)](https://travis-ci.org/netzulo/qacode)
+ 3. [qadmin](https://github.com/netzulo/qadmin) : [![Build Status](https://travis-ci.org/netzulo/qadmin.svg?branch=master)](https://travis-ci.org/netzulo/qadmin) 


## Command Usage

```
usage: qalab.py [-h] [-v] {install} ...

Performs selenium drivers operations

positional arguments:
  {install}      Install command
    install      Install selenium HUB or NODE

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  verbose level... repeat up to three times.

----- help us on , https://github.com/netzulo/qalab -------
```

## Tests

__Not defined__
