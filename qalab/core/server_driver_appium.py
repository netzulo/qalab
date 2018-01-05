
# -*- coding: utf-8 -*-
"""TODO: doc module"""


from qalab.core.server_driver_base import ServerDriverBase


class ServerDriverAppium(ServerDriverBase):
    """TODO: doc class"""

    _server_driver = 'appium'

    def __init__(self):
        """TODO: doc method"""
        super(ServerDriverAppium, self).__init__()

    def install(self):
        self._configure(self._server_driver)
