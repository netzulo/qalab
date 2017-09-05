# QA laboratory 

| Branch  | Linux Deploy | Windows Deploy |
| ------------- | ------------- |  ------------- |
| master  | [![Build Status](https://travis-ci.org/netzulo/qalab.svg?branch=master)](https://travis-ci.org/netzulo/qalab)  | [![Build status](https://ci.appveyor.com/api/projects/status/f4orjhi6vjgsxxq9/branch/master?svg=true)](https://ci.appveyor.com/project/netzulo/qalab-v060g/branch/master)  |
| devel  | [![Build Status](https://travis-ci.org/netzulo/qalab.svg?branch=devel)](https://travis-ci.org/netzulo/qalab)  | [![Build status](https://ci.appveyor.com/api/projects/status/f4orjhi6vjgsxxq9/branch/devel?svg=true)](https://ci.appveyor.com/project/netzulo/qalab-v060g/branch/devel)  |

## Code Metrics

[![umm](https://qalab.tk/api/badges/gate?key=qacode)](https://qalab.tk/api/badges/gate?key=qacode)

## _How to install ?_

+ 1. Clone this repo : `git clone https://github.com/netzulo/qalab.git`
+ 2. Enter on repo directory : `cd qalab`
+ 3. Clone submodules : `git submodule update --init --recursive`
+ 4. Attach branches HEAD: `git submodule foreach git checkout master`

## PIP install

```
pip install qalaboratory
```

## Command Usage

```
usage: qalab.py [-h] [-v] {selenium} ...

Performs selenium drivers operations

positional arguments:
  {selenium}     Actions for selenium instance
    selenium     Actions for selenium HUB or NODE
	
  selenium arguments:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  Select mode, values are: [hub, node]
  -i, --install         Download selenium jar
  -s, --start           Start Selenium jar
  -p PLATFORM, --platform PLATFORM
                          Select mode, values are: [lin32,lin64,win32,win64]

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  verbose level... repeat up to three times.

----- help us on , https://github.com/netzulo/qalab -------
```

## How to creat HUB + Node ?

### Hub

+ 1. Create configuration : `python qalab/qalab.py selenium --mode hub --install`
+ 2. Start Hub : `python qalab/qalab.py selenium --mode hub --start`

### Node

+ 1. Create configuration : `python qalab/qalab.py selenium --mode node --install`
+ 2. Start Node : `python qalab/qalab.py selenium --mode node --start --platform win64`


## SubModules

__All submodules statuses__

### qacode | **[API documentation](http://qalab.tk/qacode/)**

| Branch  | Linux Deploy | Windows Deploy |
| ------------- | ------------- |  ------------- |
| master  | [![Build Status](https://travis-ci.org/netzulo/qadoc.svg?branch=master)](https://travis-ci.org/netzulo/qacode)  | [![Build status](https://ci.appveyor.com/api/projects/status/4a0tc5pis1bykt9x/branch/master?svg=true)](https://ci.appveyor.com/project/netzulo/qacode/branch/master)  |
| devel  | [![Build Status](https://travis-ci.org/netzulo/qadmin.svg?branch=devel)](https://travis-ci.org/netzulo/qacode)  | [![Build status](https://ci.appveyor.com/api/projects/status/4a0tc5pis1bykt9x/branch/devel?svg=true)](https://ci.appveyor.com/project/netzulo/qacode/branch/devel)  |


### qadoc | **[API documentation](http://qalab.tk/qadoc/)**

| Branch  | Linux Deploy | Windows Deploy |
| ------------- | ------------- |  ------------- |
| master  | [![Build Status](https://travis-ci.org/netzulo/qadoc.svg?branch=master)](https://travis-ci.org/netzulo/qadoc)  | [![Build status](https://ci.appveyor.com/api/projects/status/o70qi0ykpagrgte2/branch/master?svg=true)](https://ci.appveyor.com/project/netzulo/qadoc/branch/master)  |
| devel  | [![Build Status](https://travis-ci.org/netzulo/qadoc.svg?branch=devel)](https://travis-ci.org/netzulo/qadoc)  | [![Build status](https://ci.appveyor.com/api/projects/status/o70qi0ykpagrgte2/branch/devel?svg=true)](https://ci.appveyor.com/project/netzulo/qadoc/branch/devel)  |


### qadmin  **[API documentation](http://qalab.tk/qadmin/)**

| Branch  | Linux Deploy | Windows Deploy |
| ------------- | ------------- |  ------------- |
| master  | [![Build Status](https://travis-ci.org/netzulo/qadmin.svg?branch=master)](https://travis-ci.org/netzulo/qadmin)  | [![Build status](https://ci.appveyor.com/api/projects/status/qrb3o3qdeg3qv9eq/branch/master?svg=true)](https://ci.appveyor.com/project/netzulo/qadmin/branch/master)  |
| devel  | [![Build Status](https://travis-ci.org/netzulo/qadmin.svg?branch=devel)](https://travis-ci.org/netzulo/qadmin)  | [![Build status](https://ci.appveyor.com/api/projects/status/qrb3o3qdeg3qv9eq/branch/devel?svg=true)](https://ci.appveyor.com/project/netzulo/qadmin/branch/devel)  |


### qadrivers  **[API documentation](http://qalab.tk/qadrivers/)**

| Drivers  | Linux 32 | Linux 64 |  Windows 32 | Windows 64 |
| ------------- | ------------- |  ------------- |  ------------- |  ------------- |
| Chrome |  OK |  OK |  OK |  OK |
| Firefox |  OK |  OK |  OK |  OK |
| PhantomJs |  OK |  OK |  OK |  OK |
| Internet Explorer |  _doesn't exist_ |  _doesn't exist_ |  OK |  OK |
| Edge |  _doesn't exist_ |  _doesn't exist_ |  OK |  OK |
