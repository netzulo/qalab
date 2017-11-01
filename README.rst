QA laboratory 
=============

+--------------+--------------------------+---------------------------+---------------------------+--------------------------+
| Branch name  | QAlab                    | QAcode                    | QAdmin                    | QAdoc                    |
+==============+==========================+===========================+===========================+==========================+
| master       | |qalab_build_master_lin| | |qacode_build_master_lin| | |qadmin_build_master_lin| | |qadoc_build_master_lin| |
|              | |qalab_build_master_win| | |qacode_build_master_win| | |qadmin_build_master_win| | |qadoc_build_master_win| |
+--------------+--------------------------+---------------------------+---------------------------+--------------------------+
| devel        | |qalab_build_devel_lin|  | |qacode_build_devel_lin|  | |qadmin_build_devel_lin|  | |qadoc_build_devel_lin|  |
|              | |qalab_build_devel_win|  | |qacode_build_devel_win|  | |qadmin_build_devel_win|  | |qadoc_build_devel_win|  |
+--------------+--------------------------+---------------------------+---------------------------+--------------------------+

Documentation
-------------

- QAlab qalab_api_
- QAcode qacode_api_
- QAdoc qadoc_api_
- QAdmin qadmin_api_ 
- QAdrivers qadrivers_api_


Code Metrics by sonarqube
----------------------------

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

PIP install
***********

``pip install qalaboratory``

Command Usage
*************

::

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


How to create HUB + Node ?
-------------------------

Hub
****

+ 1. Create configuration : ``python qalab/qalab.py selenium --mode hub --install``
+ 2. Start Hub : ``python qalab/qalab.py selenium --mode hub --start``

Node
****

+ 1. Create configuration : ``python qalab/qalab.py selenium --mode node --install``
+ 2. Start Node : ``python qalab/qalab.py selenium --mode node --start --platform win64``

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
.. _qalab_api: http://qalab.tk/qalab/
.. _qacode_api: http://qalab.tk/qacode/
.. _qadoc_api: http://qalab.tk/qadoc/
.. _qadmin_api: http://qalab.tk/qadmin/
.. _qadrivers_api: http://qalab.tk/qadrivers/
