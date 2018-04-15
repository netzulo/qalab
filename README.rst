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

Documentation
-------------

- QAlab qalab_api_
- QAcode qacode_api_
- QAtestlink qatestlink_api_
- QAdoc qadoc_api_
- QAdmin qadmin_api_ 
- QAdrivers qadrivers_api_


Code Metrics by sonarqube
-------------------------

.. image:: http://qalab.tk:82/api/badges/gate?key=qalab
  :alt: Quality Gate
  :target: http://qalab.tk:82/api/badges/gate?key=qalab
.. image:: http://qalab.tk:82/api/badges/measure?key=qalab&metric=lines
  :alt: Lines
  :target: http://qalab.tk:82/api/badges/gate?key=qalab
.. image:: http://qalab.tk:82/api/badges/measure?key=qalab&metric=bugs
  :alt: Bugs
  :target: http://qalab.tk:82/api/badges/gate?key=qalab
.. image:: http://qalab.tk:82/api/badges/measure?key=qalab&metric=vulnerabilities
  :alt: Vulnerabilities
  :target: http://qalab.tk:82/api/badges/gate?key=qalab
.. image:: http://qalab.tk:82/api/badges/measure?key=qalab&metric=code_smells
  :alt: Code Smells
  :target: http://qalab.tk:82/api/badges/gate?key=qalab
.. image:: http://qalab.tk:82/api/badges/measure?key=qalab&metric=sqale_debt_ratio
  :alt: Debt ratio
  :target: http://qalab.tk:82/api/badges/gate?key=qalab
.. image:: http://qalab.tk:82/api/badges/measure?key=qalab&metric=comment_lines_density
  :alt: Comments
  :target: http://qalab.tk:82/api/badges/gate?key=qalab


How to install ?
----------------

+ 1. *Clone this repo* : ``git clone https://github.com/netzulo/qalab.git``
+ 2. *Enter on repo directory* : ``cd qalab``
+ 3. *Clone submodules* : ``git submodule update --init --recursive``
+ 4. *Attach branches HEAD* : ``git submodule foreach git checkout master``


How to exec tests ?
-------------------

+ 1. *Clone this repo* : ``git clone https://github.com/netzulo/qalab.git``
+ 2. *Enter on repo directory* : ``cd qalab``
+ 3. *Execute test with setup.py* : ``python setup.py test``


PIP install
***********

``pip install qalaboratory``

Command Usage
*************

::

  usage: qalab.py [-h] [-v] [-sd SERVER_DRIVER] [-m MODE] [-i] [-s]
                [-p PLATFORM]

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

  ----- help us on , https://github.com/netzulo/qalab -------


How to create HUB + Node ?
-------------------------

Hub
****

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


TOX environments
****************

+---------------------+--------------------------------+
| Env name            | Env description                |
+=====================+================================+
| py27,py34,py35,py36 | Python supported versions      |
+---------------------+--------------------------------+
| docs                | Generate doc HTML in /docs     |
+---------------------+--------------------------------+
| flake8              | Exec linter in qalab/ tests/   |
+---------------------+--------------------------------+
| selenium-hub        | Start intalled selenium hub    |
+---------------------+--------------------------------+
| selenium-node       | Start intalled selenium node   |
+---------------------+--------------------------------+
| selendroid-hub      | Start intalled selendroid hub  |
+---------------------+--------------------------------+
| selendroid-node     | Start intalled selendroid node |
+---------------------+--------------------------------+
| appium-node         | Start intalled appium node     |
+---------------------+--------------------------------+


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
.. _qalab_api: http://qalab.tk/qalab/
.. _qacode_api: http://qalab.tk/qacode/
.. _qatestlink_api: http://qalab.tk/qatestlink/
.. _qadoc_api: http://qalab.tk/qadoc/
.. _qadmin_api: http://qalab.tk/qadmin/
.. _qadrivers_api: http://qalab.tk/qadrivers/
