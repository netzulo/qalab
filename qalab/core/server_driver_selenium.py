
# -*- coding: utf-8 -*-
"""TODO: doc module"""


from qalab.core.server_driver_base import ServerDriverBase
import qalab.configs.settings as SETTINGS


class ServerDriverSelenium(ServerDriverBase):
    """TODO: doc class"""

    _server_driver = 'selenium'
    _drivers_abspath = None
    

    def __init__(self, mode):
        """TODO: doc method"""
        super(ServerDriverSelenium, self).__init__(mode)
        self._drivers_abspath = self.get_abspaths()

    def install(self):
        self._configure(self._server_driver)

    def get_abspaths(self):
        """TODO: doc method"""
        drivers_abspath = []
        for driver_name in SETTINGS.DRIVERS_NAMES:
            webdriver_var_name = None
            if driver_name.startswith("chrome"):
                webdriver_var_name = SETTINGS.WEBDRIVER_ENV_VARS[0]
            if driver_name.startswith("firefox"):
                webdriver_var_name = SETTINGS.WEBDRIVER_ENV_VARS[1]
            if driver_name.startswith("phantomjs"):
                webdriver_var_name = SETTINGS.WEBDRIVER_ENV_VARS[2]
            if driver_name.startswith("iexplorer"):
                webdriver_var_name = SETTINGS.WEBDRIVER_ENV_VARS[3]
            if driver_name.startswith("edge"):
                webdriver_var_name = SETTINGS.WEBDRIVER_ENV_VARS[4]
            if driver_name.startswith("opera"):
                webdriver_var_name = SETTINGS.WEBDRIVER_ENV_VARS[5]
            # Get absolute path for driver_name
            drivers_abspath.append("{}{}{}".format(
                webdriver_var_name,
                SETTINGS.PATH_DRIVERS_MODULE,
                driver_name))
        return drivers_abspath
