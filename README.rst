QA laboratory 
=============

.. image:: https://img.shields.io/github/issues/netzulo/qalab.svg
  :alt: Issues on Github
  :target: https://github.com/netzulo/qalab/issues

.. image:: https://img.shields.io/github/issues-pr/netzulo/qalab.svg
  :alt: Pull Request opened on Github
  :target: https://github.com/netzulo/qalab/issues

.. image:: https://img.shields.io/github/release/netzulo/qalab.svg
  :alt: Release version on Github
  :target: https://github.com/netzulo/qalab/releases/latest

.. image:: https://img.shields.io/github/release-date/netzulo/qalab.svg
  :alt: Release date on Github
  :target: https://github.com/netzulo/qalab/releases/latest

+--------------+--------------------------+---------------------------+---------------------------+--------------------------+--------------------------+
| Branch name  | QAlab                    | QAcode                    | QAdmin                    | QAdoc                    | QAtestlink               |
+==============+==========================+===========================+===========================+==========================+==========================+
| master       | |qalab_build_master_lin| | |qacode_build_master_lin| | |qadmin_build_master_lin| | |qadoc_build_master_lin| | |qadoc_build_master_lin| |
|              | |qalab_build_master_win| | |qacode_build_master_win| | |qadmin_build_master_win| | |qadoc_build_master_win| | |qadoc_build_master_win| |
+--------------+--------------------------+---------------------------+---------------------------+--------------------------+--------------------------+


How to install ?
----------------

+ 1. *Clone this repo* : ``git clone https://github.com/netzulo/qalab.git``
+ 2. *Enter on repo directory* : ``cd qalab``
+ 3. *Clone submodules* : ``git submodule update --init --recursive``
+ 4. *Attach branches HEAD* : ``git submodule foreach git checkout master``
+ 5. *Install qalab package*: from PIP ``pip install qalaboratory`` or from setup.py file ``python setup.py install``


Command Usage
*************

::

  usage: qaenv.py [-h] [-v] [-sd SERVER_DRIVER] [-m MODE] [-i] [-s]
                  [-p PLATFORM] [-dcp DRIVER_CONFIG_PATH]
  
  Performs selenium drivers operations
  
  optional arguments:
    -h, --help            show this help message and exit
    -v, --verbose         verbose level... repeat up to three times.
    -sd SERVER_DRIVER, --server_driver SERVER_DRIVER
                          Select server driver, values are:
                          [selenium,appium,selendroid]
    -m MODE, --mode MODE  Select mode, values are: [hub, node]
    -i, --install         Download driver server jar
    -s, --start           Start driver server jar
    -p PLATFORM, --platform PLATFORM
                          Select mode, values are: [lin32,lin64,win32,win64]
    -dcp DRIVER_CONFIG_PATH, --driver_config_path DRIVER_CONFIG_PATH
                          Use different absolute PATH+FILE_NAME to read
                          DRIVER_CONFIG
  
  ----- help us on , https://github.com/netzulo/qalab -------


How to create HUB + Node ?
--------------------------

Hub
***

+ 1. Create configuration : ``python qalab/qaenv.py --server_driver selenium --mode hub --install``
+ 2. Start Hub : ``python qalab/qaenv.py --server_driver selenium --mode hub --start``

Node
****

+ 1. Create configuration : ``python qalab/qaenv.py --server_driver selenium --mode node --install``
+ 2. Start Node : ``python qalab/qaenv.py selenium --server_driver selenium --mode node --start --platform win64``

Appium
******

*Must be installed SDK and appium (from NPM) as global package*

+ 1. Install SDK
+ 2. Install appium: ``npm install -g appium``
+ 3. Create configuration : ``python qalab/qaenv.py --server_driver appium --mode node --install``
+ 4. Start Node : ``python qalab/qaenv.py --server_driver appium --mode node --start --platform win64``


How to exec tests ?
-------------------

+ Tests from setup.py file : ``python setup.py test``

+ Install from PIP file : ``pip install tox``
+ Tests from tox : ``tox -l && tox -e TOX_ENV_NAME`` ( *see tox.ini file to get environment names* )


+--------------------------+--------------------------------+
| TOX Env name             | Env description                |
+==========================+================================+
| py27,py34,py35,py36,py37 | Python supported versions      |
+--------------------------+--------------------------------+
| flake8                   | Exec linter in qalab/ tests/   |
+--------------------------+--------------------------------+
| coverage                 | Generate XML and HTML reports  |
+--------------------------+--------------------------------+
| docs                     | Generate doc HTML in /docs     |
+--------------------------+--------------------------------+
| selenium-hub             | Start intalled selenium hub    |
+--------------------------+--------------------------------+
| selenium-node            | Start intalled selenium node   |
+--------------------------+--------------------------------+
| selendroid-hub           | Start intalled selendroid hub  |
+--------------------------+--------------------------------+
| selendroid-node          | Start intalled selendroid node |
+--------------------------+--------------------------------+
| appium-node              | Start intalled appium node     |
+--------------------------+--------------------------------+
| selenium-tests           | Execute Hub+Node tests         |
+--------------------------+--------------------------------+


QADrivers
*********

+-------------------+----------+----------+------------+------------+
| Drivers           | Linux 32 | Linux 64 | Windows 32 | Windows 64 |
+===================+==========+==========+============+============+
| Chrome            | OK       | OK       | OK         | OK         |
+-------------------+----------+----------+------------+------------+
| Firefox           | OK       | OK       | OK         | OK         |
+-------------------+----------+----------+------------+------------+
| PhantomJs         | OK       | OK       | OK         | OK         |
+-------------------+----------+----------+------------+------------+
| Internet Explorer | -        | -        | OK         | OK         |
+-------------------+----------+----------+------------+------------+
| Edge              | -        | -        | OK         | OK         |
+-------------------+----------+----------+------------+------------+
| Android           | OK       | OK       | OK         | OK         |
+-------------------+----------+----------+------------+------------+


.. |qalab_build_master_lin| image:: https://travis-ci.org/netzulo/qalab.svg?branch=master
.. |qalab_build_master_win| image:: https://ci.appveyor.com/api/projects/status/f4orjhi6vjgsxxq9/branch/master?svg=true
.. |qalab_build_devel_lin| image:: https://travis-ci.org/netzulo/qalab.svg?branch=devel
.. |qalab_build_devel_win| image:: https://ci.appveyor.com/api/projects/status/f4orjhi6vjgsxxq9/branch/devel?svg=true
.. |qacode_build_master_lin| image:: https://travis-ci.org/netzulo/qacode.svg?branch=master
.. |qacode_build_master_win| image:: https://ci.appveyor.com/api/projects/status/4a0tc5pis1bykt9x/branch/master?svg=true
.. |qacode_build_devel_lin| image:: https://travis-ci.org/netzulo/qacode.svg?branch=devel
.. |qacode_build_devel_win| image:: https://ci.appveyor.com/api/projects/status/4a0tc5pis1bykt9x/branch/devel?svg=true
.. |qadoc_build_master_lin| image:: https://travis-ci.org/netzulo/qadoc.svg?branch=master 
.. |qadoc_build_master_win| image:: https://ci.appveyor.com/api/projects/status/o70qi0ykpagrgte2/branch/master?svg=true
.. |qadoc_build_devel_lin| image:: https://travis-ci.org/netzulo/qadoc.svg?branch=devel
.. |qadoc_build_devel_win| image:: https://ci.appveyor.com/api/projects/status/o70qi0ykpagrgte2/branch/devel?svg=true
.. |qadmin_build_master_lin| image:: https://travis-ci.org/netzulo/qadmin.svg?branch=master
.. |qadmin_build_master_win| image:: https://ci.appveyor.com/api/projects/status/qrb3o3qdeg3qv9eq/branch/master?svg=true
.. |qadmin_build_devel_lin| image:: https://travis-ci.org/netzulo/qadmin.svg?branch=devel
.. |qadmin_build_devel_win| image:: https://ci.appveyor.com/api/projects/status/qrb3o3qdeg3qv9eq/branch/devel?svg=true
.. |qatestlink_build_master_lin| image:: https://travis-ci.org/netzulo/qatestlink.svg?branch=master
.. |qatestlink_build_master_win| image:: https://ci.appveyor.com/api/projects/status/kw4si7if8lw7m10n/branch/master?svg=true
.. |qatestlink_build_devel_lin| image:: https://travis-ci.org/netzulo/qatestlink.svg?branch=devel
.. |qatestlink_build_devel_win| image:: https://ci.appveyor.com/api/projects/status/kw4si7if8lw7m10n/branch/devel?svg=true
