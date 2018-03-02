
# -*- coding: utf-8 -*-
"""package for manage selenium drivers and actions"""


from qalab.core.server_driver_base import ServerDriverBase


class ServerDriverAppium(ServerDriverBase):
    """
    Class manager for selenium
     drivers with customizable configuration
    """

    server_driver = 'appium'
    drivers_abspath = None
    platforms = ["win32", "win64", "lin32", "lin64"]
    cmd_args = ["appium"]

    def __init__(self, logger, mode, driver_config_path=None):
        """
        Start server_driver for appium with logger and custom mode
        :args:
            logger: python logging class
            mode: valid values are 'hub', 'node'
        """
        super(ServerDriverAppium, self).__init__(
            logger, mode, driver_config_path=driver_config_path)

    def install(self):
        """Install proccess for appium server_driver"""
        if self._mode == 'hub':
            raise NotImplementedError(
                'Still not developed, open issue on github if you got this')
        super(ServerDriverAppium, self)._configure(self.server_driver)
        self.logger.info(
            'Command install: need NPM and global appium installed')

    def start(self, platform):
        """Start proccess for appium server_driver"""
        if self._mode == 'hub':
            raise NotImplementedError(
                'Still not developed, open issue on github if you got this')
        super(ServerDriverAppium, self)._configure(
            self.server_driver, copy=False)
        self.logger.info('Command start: ...')
        cmd_default_args = [
            "--{}config".format(self._mode), self._config_path
        ]
        # start driver_server with arguments
        self.cmd_args.extend(cmd_default_args)
        self.command_exec(self.cmd_args, shell=True)
        self.logger.info("Command start : DONE")
