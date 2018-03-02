
# -*- coding: utf-8 -*-
"""package for manage selenium drivers and actions"""


import os
import qalab.configs.settings as SETTINGS
from qalab.core.server_driver_base import ServerDriverBase


class ServerDriverSelenium(ServerDriverBase):
    """
    Class manager for selenium
     drivers with customizable configuration
    """

    server_driver = 'selenium'
    drivers_abspath = None
    platforms = ["win32", "win64", "lin32", "lin64"]
    cmd_args = ["java"]

    def __init__(self, logger, mode, driver_config_path=None):
        """
        Start server_driver for selenium with logger and custom mode
        :args:
            logger: python logging class
            mode: valid values are 'hub', 'node'
        """
        super(ServerDriverSelenium, self).__init__(
            logger, mode, driver_config_path=driver_config_path)
        self.drivers_abspath = self.get_abspaths()

    def install(self):
        """Install proccess for selenium server_driver"""
        super(ServerDriverSelenium, self)._configure(self.server_driver)
        self.logger.info('Command install: ...')
        jar_path = "{}/{}".format(
            SETTINGS.PATH_SERVER_DRIVERS,
            SETTINGS.SELENIUM_JAR_NAME)
        if os.path.exists(jar_path):
            self.logger.warning('File exist, not downloading')
            self.logger.debug('  at path={}'.format(jar_path))
        else:
            self.download_file(SETTINGS.SELENIUM_URL, jar_path)
        self.logger.info('Command install: DONE')

    def start(self, platform):
        """Start proccess for selenium server_driver"""
        super(ServerDriverSelenium, self)._configure(
            self.server_driver, copy=False)
        self.logger.info('Command start: ...')
        cmd_default_args = [
            "-jar", "{}/{}".format(
                SETTINGS.PATH_SERVER_DRIVERS,
                SETTINGS.SELENIUM_JAR_NAME),
            "-role", self._mode,
            "-{}Config".format(self._mode), self._config_path,
            "-log", "logs/selenium.{}.log".format(self._mode)
        ]
        if self._mode == 'node':
            if platform is None or platform not in self.platforms:
                self.logger.error(SETTINGS.MSG_PLATFORM_ERROR)
                return
            # merge drivers args
            self.cmd_args.extend(self.args_drivers(platform))
        # merge default args
        self.cmd_args.extend(cmd_default_args)
        self.logger.info('Command start: DONE')
        self.command_exec(self.cmd_args)

    def args_drivers(self, platform):
        """
        Get a list of drivers absolute
         paths filtered by platform
        """
        cmd_drivers = []
        if self._mode == "node":
            if platform == "win32":
                cmd_drivers.extend(
                    self.name_filter_win32(self.drivers_abspath))
            elif platform == "win64":
                cmd_drivers.extend(
                    self.name_filter_win64(self.drivers_abspath))
            elif platform == "lin32":
                cmd_drivers.extend(
                    self.name_filter_lin32(self.drivers_abspath))
            elif platform == "lin64":
                cmd_drivers.extend(
                    self.name_filter_lin64(self.drivers_abspath))
        return cmd_drivers

    def get_abspaths(self):
        """Get drivers names with absolute paths"""
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

    def name_filter_lin64(self, drivers_abspaths):
        """Return array ofparsed absolute paths name for platform LINUX 64"""
        return [
            self.name_filter(self.drivers_abspath, "chromedriver_64"),
            self.name_filter(self.drivers_abspath, "firefoxdriver_64"),
            self.name_filter(self.drivers_abspath, "phantomjsdriver_64"),
            self.name_filter(self.drivers_abspath, "operadriver_64")
        ]

    def name_filter_lin32(self, drivers_abspaths):
        """Return array ofparsed absolute paths name for platform LINUX 32"""
        return [
            self.name_filter(self.drivers_abspath, "chromedriver_32"),
            self.name_filter(self.drivers_abspath, "firefoxdriver_32"),
            self.name_filter(self.drivers_abspath, "phantomjsdriver_32"),
            self.name_filter(self.drivers_abspath, "operadriver_32")
        ]

    def name_filter_win64(self, drivers_abspaths):
        """Return array ofparsed absolute paths name for platform WINDOWS 64"""
        return [
            self.name_filter(self.drivers_abspath, "chromedriver_32.exe"),
            self.name_filter(self.drivers_abspath, "firefoxdriver_64.exe"),
            self.name_filter(self.drivers_abspath, "phantomjsdriver_64.exe"),
            self.name_filter(self.drivers_abspath, "iexplorerdriver_64.exe"),
            self.name_filter(self.drivers_abspath, "edgedriver_64.exe"),
            self.name_filter(self.drivers_abspath, "operadriver_64.exe")
        ]

    def name_filter_win32(self, drivers_abspaths):
        """Return array ofparsed absolute paths name for platform WINDOWS 32"""
        return [
            self.name_filter(self.drivers_abspath, "chromedriver_32.exe"),
            self.name_filter(self.drivers_abspath, "firefoxdriver_32.exe"),
            self.name_filter(self.drivers_abspath, "phantomjsdriver_32.exe"),
            self.name_filter(self.drivers_abspath, "iexplorerdriver_32.exe"),
            self.name_filter(self.drivers_abspath, "operadriver_32.exe")
        ]

    def name_filter(self, names, endswith):
        """Filter for name ending with text filter"""
        names = list(names)
        _name = None
        for name in names:
            if name.endswith(endswith):
                return name
            _name = name
        raise Exception('Driver name \'{}\' not found at list'.format(_name))
