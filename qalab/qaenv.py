# -*- coding: utf-8 -*-
#! /usr/bin/env python
""""TODO: doc module"""


import argparse
import logging
import logging.handlers
import os
import shutil
import sys
import wget
from qalab.core.server_driver_selenium import ServerDriverSelenium
from qalab.core.server_driver_appium import ServerDriverAppium


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
    elif args.server_driver == 'selendroid':
        # FIX: errored
        command_selendroid(args, logger)
    elif args.server_driver == 'appium':
        command_appium(args, logger)
    else:
        logger.error(str(MSG_UNKOWN_COMMAND.format(args)))

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
        help="Select server driver, values are: [selenium,selendroid,appium]")
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
        default=None, help="Select mode, values are: [lin32,lin64,win32,win64]")
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


def command_appium(args, logger):
    """Command with appium standalone node client"""
    if args.mode not in ['hub', 'node']:
        raise Exception('Select valid mode, values are: [hub, node]')
    config_src = DRIVER_CONFIG_PATH_EXAMPLE.format(
        PATH_CONFIG, 'appium', args.mode)
    config_dst = DRIVER_CONFIG_PATH.format(
        PATH_CONFIG, 'appium', args.mode)
    if args.install:
        copy_config(logger, config_src, config_dst)
    elif args.start:
        command_start_appium(args, logger)
    else:
        logger.error("ACTION not selected: --install , --start")

def command_start_appium(args, logger):
    """TODO: doc method"""
    logger.info("Command start : ...")
    cmd_args = ["appium"]
    if args.mode == 'hub':
        raise NotImplementedError('Mode hub for appium not developed yet')
    elif args.mode == 'node':
        cmd_default_args = [
            '--nodeconfig', "{}/{}".format(PATH_CONFIG, 'appium.node.json')
        ]
    else:
        raise Exception('Select valid mode, values are: [hub, node]')
    # start driver_server with arguments
    cmd_args.extend(cmd_default_args)
    logger.debug("command info : {}".format(cmd_args))
    subprocess.call(cmd_args, shell=True)
    logger.info("Command start : DONE")


def command_selendroid(args, logger):
    """Command with selendroid standalone jar file"""
    # installation starts...
    if args.mode not in ['hub', 'node']:
        raise Exception('Select valid mode, values are: [hub, node]')
    config_src = DRIVER_CONFIG_PATH_EXAMPLE.format(
        PATH_CONFIG, 'selendroid', args.mode)
    config_dst = DRIVER_CONFIG_PATH.format(
        PATH_CONFIG, 'selendroid', args.mode)
    # TODO: generate apks names with absolute paths
    if args.install:
        if args.mode == 'node':
            command_install(
                args, logger, SELENDROID_URL, SELENDROID_JAR,
                config_src, config_dst)
            command_install(
                args, logger, SELENDROID_PLUGIN_URL, SELENDROID_PLUGIN_JAR,
                config_src, config_dst)
        elif args.mode == 'hub':
            command_install(args, logger, SELENDROID_SELENIUM_URL, SELENDROID_SELENIUM_JAR, config_src, config_dst)
    elif args.start:
        command_start_selendroid(args, logger)
    else:
        logger.error("ACTION not selected: --install , --start")

def command_selenium(args, logger):
    """Command with selenium standalone jar file"""
    server_driver = ServerDriverSelenium(logger, args.mode)
    if args.install:
        server_driver.install()
    elif args.start:
        server_driver.start()
    else:
        logger.error("ACTION not selected: --install , --start")

def command_start_selendroid(args, logger):
    """TODO: doc method"""
    cmd_args = ["java"]
    config_dst = DRIVER_CONFIG_PATH_EXAMPLE.format(
        PATH_CONFIG, 'selendroid', args.mode)
    if args.mode == 'hub':
        cmd_default_args = [
            "-Dfile.encoding=UTF-8",
            "-cp",
            "\"{}:{}\" org.openqa.grid.selenium.GridLauncher".format(
                "{}/{}".format(PATH_SERVER_DRIVERS, SELENDROID_PLUGIN_JAR),
                "{}/{}".format(PATH_SERVER_DRIVERS, SELENDROID_SELENIUM_JAR)
            ),
            "-jar", "{}/{}".format(PATH_SERVER_DRIVERS, SELENDROID_JAR),
            "-role", args.mode,
            "-{}Config".format(args.mode), config_dst,
            "-log", "logs/selendroid.{}.log".format(args.mode)
        ]
    elif args.mode == 'node':
        cmd_default_args = [
            "-jar", "{}/{}".format(PATH_SERVER_DRIVERS, SELENDROID_JAR),
            "-port", "12001",
            "-selendroidServerPort", SELENDROID_PORT,
            "-folder", os.path.abspath(PATH_APKS),
            "-logLevel", "DEBUG",
            "-proxy", "io.selendroid.grid.SelendroidSessionProxy",
        ]
    else:
        raise Exception('Select valid mode, values are: [hub, node]')
    # start driver_server with arguments
    cmd_args.extend(cmd_default_args)
    logger.info("Executing command : {}".format(cmd_args))
    return subprocess.call(cmd_args)

def command_install(args, logger, url, jar_name, config_src, config_dst):
    """TODO: doc method"""
    logger.info('Command install: ...')
    jar_path = "{}/{}".format(PATH_SERVER_DRIVERS, jar_name)
    if os.path.exists(jar_path):
        logger.info('File exist')
        logger.debug('  at path={}'.format(jar_path))
    else:
        download_file(logger, url, jar_path)
    copy_config(logger, config_src, config_dst)
    logger.info('Command install: DONE')



def set_log_level_from_verbose(console_handler, args, logger):
    """Logging level handler for script"""
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
