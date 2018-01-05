
# -*- coding: utf-8 -*-
"""TODO: doc module"""


from qalab.core.server_driver_base import ServerDriverBase


class ServerDriverSelendroid(ServerDriverBase):
    """TODO: doc class"""

    _server_driver = 'selendroid'

    def __init__(self, mode):
        """TODO: doc method"""
        super(ServerDriverSelendroid, self).__init__(mode)

    def install(self):
        self._configure(self._server_driver)
