# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""TODO: doc module"""


import argparse
import logging
import logging.handlers
import os
import sys
import qalab.configs.settings as SETTINGS
from qalab.core.server_driver_appium import ServerDriverAppium
from qalab.core.server_driver_selenium import ServerDriverSelenium


def main(args=None):
    """TODO: doc method"""
    if args is None:
        args = sys.argv[1:]
    # Generate parser
    parser = parser_instance()
    args = parser.parse_args()
    # Generate logger
    logger = logger_instance(args)
    # START SCRIPT
    if args.server_driver is None:
        logger.error("can't start without server_driver name, option: -sd")
        return
    if args.server_driver == 'selenium':
        command_selenium(args, logger)
    elif args.server_driver == 'appium':
        command_appium(args, logger)
    elif args.server_driver == 'selendroid':
        command_selendroid(args, logger)
    else:
        logger.error(str(SETTINGS.MSG_UNKOWN_COMMAND.format(args)))


def parser_instance():
    """TODO: doc method"""
    parser = argparse.ArgumentParser(
        description="Performs selenium drivers operations",
        epilog="----- help us on , https://github.com/netzulo/qalab -------",
        fromfile_prefix_chars='@',)
    # Main args
    parser.add_argument(
        '-v', '--verbose',
        action="count", help="verbose level... repeat up to three times.")
    parser.add_argument(
        '-sd', '--server_driver',
        default=None,
        help="Select server driver, values are: [selenium,appium,selendroid]")
    # Optional args
    parser.add_argument(
        '-m', '--mode',
        default=None, help="Select mode, values are: [hub, node]")
    parser.add_argument(
        '-i', '--install',
        action="store_true", help="Download driver server jar")
    parser.add_argument(
        '-s', '--start',
        action="store_true", help="Start driver server jar")
    parser.add_argument(
        '-p', '--platform',
        default=None,
        help="Select mode, values are: [lin32,lin64,win32,win64]")
    parser.add_argument(
        '-dcp', '--driver_config_path',
        default=None,
        help="Use different absolute PATH+FILE_NAME to read DRIVER_CONFIG")
    return parser


def logger_instance(args):
    """TODO: doc method"""
    msg_file_formatter = "{} [{}]({}:{}:{}): {}".format(
        "%(asctime)s", "%(levelname)s", "%(name)s",
        "%(funcName)s", "%(lineno)d", "%(message)s"
    )
    msg_console_formatter = '[%(levelname)s](%(name)s): %(message)s'
    logger = logging.getLogger('qalab')
    logger.setLevel(logging.DEBUG)
    if not os.path.exists('../logs'):
        os.mkdir('../logs')
    log_file_handler = logging.handlers.TimedRotatingFileHandler(
        '../logs/qalab.log', when='M', interval=2)
    log_file_handler.setFormatter(logging.Formatter(msg_file_formatter))
    log_file_handler.setLevel(logging.DEBUG)
    logger.addHandler(log_file_handler)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.CRITICAL)
    console_handler.setFormatter(logging.Formatter(msg_console_formatter))
    logger.addHandler(console_handler)
    set_log_level_from_verbose(console_handler, args, logger)
    return logger


def command_selenium(args, logger):
    """Command with selenium standalone jar file"""
    server_driver = ServerDriverSelenium(
        logger, args.mode, driver_config_path=args.driver_config_path)
    if args.install:
        server_driver.install()
    elif args.start:
        server_driver.start(args.platform)
    else:
        logger.error("ACTION not selected: --install , --start")


def command_appium(args, logger):
    """Command with appium standalone node client"""
    server_driver = ServerDriverAppium(
        logger, args.mode, driver_config_path=args.driver_config_path)
    if args.install:
        server_driver.install()
    elif args.start:
        server_driver.start(args.platform)
    else:
        logger.error("ACTION not selected: --install , --start")


def command_selendroid(args, logger):
    """Command with selendroid+plugin standalone jar file"""
    logger.error(
        """server_driver not developed yet,
        open issue on github if you got this""")


def set_log_level_from_verbose(console_handler, args, logger):
    """Set logging level handler for script"""
    if not args.verbose:
        console_handler.setLevel("INFO")
    elif args.verbose == 1:
        console_handler.setLevel('WARNING')
    elif args.verbose == 2:
        console_handler.setLevel('INFO')
    elif args.verbose >= 3:
        console_handler.setLevel('DEBUG')
    else:
        logger.critical("LOGGER level doesn't exist")


if __name__ == '__main__':
    main()
