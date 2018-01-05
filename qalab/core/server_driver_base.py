
# -*- coding: utf-8 -*-
"""TODO: doc module"""


import qalab.configs.settings as SETTINGS
import shutil


class ServerDriverBase(object):
    """TODO: doc class"""

    _mode = None
    _config_src = None
    _config_dst = None
    _server_driver = 'base'


    def __init__(self, mode):
        """TODO: doc method"""
        if mode is None:
            raise Exception("param 'mode' can't be None")
        if mode not in ['hub', 'node']:
            raise Exception('Select valid mode, values are: [hub, node]')
        self._mode = mode
        _config_path_example = SETTINGS.DRIVER_CONFIG_PATH_EXAMPLE
        _config_path = SETTINGS.DRIVER_CONFIG_PATH

    def _configure(self, server_driver):
        """
        Just copy settings from example file
          from: {server_driver}.{args.mode}.example.json
          to:   {server_driver}.{args.mode}.json
        """
        if server_driver not in ['selenium', 'selendroid', 'appium']:
            raise Exception(
                'Select valid mode, values are: [selenium, selendroid, appium]'
            )
        self._config_path_example = self._config_path_example.format(
            SETTINGS.PATH_CONFIG, server_driver, self._mode)
        self._config_path = self._config_path.format(
            SETTINGS.PATH_CONFIG, server_driver, self._mode)
        shutil.copy2(
            self._config_path_example,
            self._config_path)

    def install(self):
        """Installation process"""
        raise NotImplementedError('need to be overrided on inherit classes')

    def start(self):
        """Installation process"""
        raise NotImplementedError('need to be overrided on inherit classes')
