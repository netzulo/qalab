# QA laboratory 

| Branch  | Linux Deploy | Windows Deploy |
| ------------- | ------------- |  ------------- |
| master  | [![Build Status](https://travis-ci.org/netzulo/qalab.svg?branch=master)](https://travis-ci.org/netzulo/qalab)  | [![Build status](https://ci.appveyor.com/api/projects/status/f4orjhi6vjgsxxq9/branch/master?svg=true)](https://ci.appveyor.com/project/netzulo/qalab-v060g/branch/master)  |
| devel  | [![Build Status](https://travis-ci.org/netzulo/qalab.svg?branch=devel)](https://travis-ci.org/netzulo/qalab)  | [![Build status](https://ci.appveyor.com/api/projects/status/f4orjhi6vjgsxxq9/branch/devel?svg=true)](https://ci.appveyor.com/project/netzulo/qalab-v060g/branch/devel)  |


## _How to install ?_

+ 1. Clone this repo : `git clone https://github.com/netzulo/qalab.git`
+ 2. Enter on repo directory : `cd qalab`
+ 3. Clone submodules : `git submodule update --init --recursive`
+ 4. Attach branches HEAD: `git submodule foreach git checkout master`

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

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  verbose level... repeat up to three times.

----- help us on , https://github.com/netzulo/qalab -------
```

## SubModules

__All submodules statuses__

### qacode | **[API documentation](http://qalab.tk:4567/qacode/)**

| Branch  | Linux Deploy | Windows Deploy |
| ------------- | ------------- |  ------------- |
| master  | [![Build Status](https://travis-ci.org/netzulo/qadoc.svg?branch=master)](https://travis-ci.org/netzulo/qacode)  | [![Build status](https://ci.appveyor.com/api/projects/status/4a0tc5pis1bykt9x/branch/master?svg=true)](https://ci.appveyor.com/project/netzulo/qacode/branch/master)  |
| devel  | [![Build Status](https://travis-ci.org/netzulo/qadmin.svg?branch=devel)](https://travis-ci.org/netzulo/qacode)  | [![Build status](https://ci.appveyor.com/api/projects/status/4a0tc5pis1bykt9x/branch/devel?svg=true)](https://ci.appveyor.com/project/netzulo/qacode/branch/devel)  |


### qadoc | **[API documentation](http://qalab.tk:4567/qadoc/)**

| Branch  | Linux Deploy | Windows Deploy |
| ------------- | ------------- |  ------------- |
| master  | [![Build Status](https://travis-ci.org/netzulo/qadoc.svg?branch=master)](https://travis-ci.org/netzulo/qadoc)  | [![Build status](https://ci.appveyor.com/api/projects/status/o70qi0ykpagrgte2/branch/master?svg=true)](https://ci.appveyor.com/project/netzulo/qadoc/branch/master)  |
| devel  | [![Build Status](https://travis-ci.org/netzulo/qadoc.svg?branch=devel)](https://travis-ci.org/netzulo/qadoc)  | [![Build status](https://ci.appveyor.com/api/projects/status/o70qi0ykpagrgte2/branch/devel?svg=true)](https://ci.appveyor.com/project/netzulo/qadoc/branch/devel)  |


### qadmin  **[API documentation](http://qalab.tk:4567/qadmin/)**

| Branch  | Linux Deploy | Windows Deploy |
| ------------- | ------------- |  ------------- |
| master  | [![Build Status](https://travis-ci.org/netzulo/qadmin.svg?branch=master)](https://travis-ci.org/netzulo/qadmin)  | [![Build status](https://ci.appveyor.com/api/projects/status/qrb3o3qdeg3qv9eq/branch/master?svg=true)](https://ci.appveyor.com/project/netzulo/qadmin/branch/master)  |
| devel  | [![Build Status](https://travis-ci.org/netzulo/qadmin.svg?branch=devel)](https://travis-ci.org/netzulo/qadmin)  | [![Build status](https://ci.appveyor.com/api/projects/status/qrb3o3qdeg3qv9eq/branch/devel?svg=true)](https://ci.appveyor.com/project/netzulo/qadmin/branch/devel)  |


