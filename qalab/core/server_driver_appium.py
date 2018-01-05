
# -*- coding: utf-8 -*-
"""TODO: doc module"""


from qalab.core.server_driver_base import ServerDriverBase


class ServerDriverAppium(ServerDriverBase):
    """TODO: doc class"""

    _server_driver = 'appium'

    def __init__(self, logger, mode):
        """TODO: doc method"""
        super(ServerDriverAppium, self).__init__(logger, mode)

    def install(self):
        """Install proccess for selenium server_driver"""
        super(ServerDriverSelenium, self)._configure(self.server_driver)
        self.logger.info('Command install: ...')
        self.logger.info('Command install: DONE')

    def start(self, platform):
        """Start proccess for selenium server_driver"""
        # TODO: noqa
