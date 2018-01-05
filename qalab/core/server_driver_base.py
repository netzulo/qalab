
# -*- coding: utf-8 -*-
"""TODO: doc module"""


import os
import shutil
import subprocess
import wget
import qalab.configs.settings as SETTINGS


class ServerDriverBase(object):
    """TODO: doc class"""

    _mode = None
    _config_src = None
    _config_dst = None
    _server_driver = 'base'


    def __init__(self, logger, mode):
        """TODO: doc method"""
        if logger is None:
            raise Exception("param 'logger' can't be None")
        self.logger = logger
        if mode is None:
            raise Exception("param 'mode' can't be None")
        if mode not in ['hub', 'node']:
            raise Exception('Select valid mode, values are: [hub, node]')
        self._mode = mode
        self._config_path_example = SETTINGS.DRIVER_CONFIG_PATH_EXAMPLE
        self._config_path = SETTINGS.DRIVER_CONFIG_PATH

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
        self.logger.info('Configuring server_driver={}'.format(server_driver))
        self._config_path_example = self._config_path_example.format(
            SETTINGS.PATH_CONFIG, server_driver, self._mode)
        self._config_path = self._config_path.format(
            SETTINGS.PATH_CONFIG, server_driver, self._mode)
        if os.path.exists(self._config_path):
            self.logger.warning('File exist, not copying from example')
        else:
            shutil.copy2(
                self._config_path_example,
                self._config_path)

    def install(self):
        """Installation process"""
        raise NotImplementedError(
            'need to be overrided on inherit classes')

    def start(self):
        """Installation process"""
        raise NotImplementedError(
            'need to be overrided on inherit classes')

    def download_file(self, url, out_path):
        """
        Download file from 'url' to 'out_path'
         logging process start and end
        """
        self.logger.info('Downloading file: ...')
        self.logger.debug('  url={}'.format(url))
        self.logger.debug('  out_path={}'.format(out_path))
        wget.download(url, out=out_path)
        self.logger.info('Downloading file: DONE')

    def command_exec(self, cmd_args):
        try:
            logger.info("Executing command : {}".format(cmd_args))
            return subprocess.call(cmd_args)
        except Exception as err:
            raise Exception(
                "Failed at handle command: {}".format(cmd_args))