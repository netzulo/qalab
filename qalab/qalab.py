# -*- coding: utf-8 -*-
#! /usr/bin/env python
""""TODO: doc module"""


import argparse
import logging
import logging.handlers
import os
import shutil
import sys
import subprocess
import wget

# SETTINGS start
PATH_CONFIG = 'qalab/configs'
PATH_DRIVERS_MODULE = 'modules/qadrivers/'
PATH_SERVER_DRIVERS = 'qalab/drivers'
WEBDRIVER_ENV_VARS = [
    "-Dwebdriver.chrome.driver=",
    "-Dwebdriver.gecko.driver=",
    "-Dphantomjs.binary.path=",
    "-Dwebdriver.ie.driver=",
    "-Dwebdriver.edge.driver="
]
DRIVERS_NAMES = [
        "chromedriver_32.exe", "chromedriver_64.exe",
        "chromedriver_32", "chromedriver_64",
        "firefoxdriver_32.exe", "firefoxdriver_64.exe",
        "firefoxdriver_32", "firefoxdriver_64",
        "phantomjsdriver_32.exe", "phantomjsdriver_64.exe",
        "phantomjsdriver_32", "phantomjsdriver_64",
        "iexplorerdriver_32.exe", "iexplorerdriver_64.exe",
        "edgedriver_32.exe", "edgedriver_64.exe"
    ]
# SETTINGS end


def main(args=None):
    """TODO: doc method"""
    msg_unkown_command = "Unknown command : {}"
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
        handle_command_selenium(args, logger)
    if args.server_driver == 'selendroid':
        handle_command_selendroid(args, logger)
    else:
        logger.error(str(msg_unkown_command.format(args)))

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
        default=None, help="Select server driver, values are: [selenium,selendroid]")
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
        "%(asctime)s",
        "%(levelname)s",
        "%(name)s",
        "%(funcName)s",
        "%(lineno)d",
        "%(message)s"
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

def handle_command_selendroid(args, logger):
    """Command with selendroid standalone jar file"""
    version = '0.17.0'
    jar_name = 'selendroid-standalone-{}-with-dependencies.jar'.format(version)
    url_base = 'https://github.com/selendroid/selendroid/releases/download/{}/{}'.format(version,jar_name)
    if args.mode not in ['hub', 'node']:
        raise Exception('Select valid mode, values are: [hub, node]')
    config_src = "{}/selendroid.{}.example.json".format(PATH_CONFIG, args.mode)
    config_dst = "{}/selendroid.{}.json".format(PATH_CONFIG, args.mode)

    logger.error("selendroid not working yet")
    raise NotImplementedError("selendroid not working yet")

def handle_command_selenium(args, logger):
    """Command with selenium standalone jar file"""
    version = "3.5"
    version_build = "3.5.3"
    jar_name = "selenium-server-standalone-{}.jar".format(version_build)
    url_base = "https://selenium-release.storage.googleapis.com/{}/{}".format(
        version, jar_name)
    # required --mode param
    if args.mode not in ['hub', 'node']:
        raise Exception('Select valid mode, values are: [hub, node]')
    config_src = "{}/selenium.{}.example.json".format(PATH_CONFIG, args.mode)
    config_dst = "{}/selenium.{}.json".format(PATH_CONFIG, args.mode)
    # generate drivers names with absolute paths
    drivers_abspaths = []
    for driver_name in DRIVERS_NAMES:
        webdriver_var_name = None
        if driver_name.startswith("chrome"):
            webdriver_var_name = WEBDRIVER_ENV_VARS[0]
        if driver_name.startswith("firefox"):
            webdriver_var_name = WEBDRIVER_ENV_VARS[1]
        if driver_name.startswith("phantomjs"):
            webdriver_var_name = WEBDRIVER_ENV_VARS[2]
        if driver_name.startswith("iexplorer"):
            webdriver_var_name = WEBDRIVER_ENV_VARS[3]
        if driver_name.startswith("edge"):
            webdriver_var_name = WEBDRIVER_ENV_VARS[4]
        # Get absolute path for driver_name
        drivers_abspaths.append(get_driver_abspath(
            webdriver_var_name, PATH_DRIVERS_MODULE, driver_name))

    if args.install:
        handle_command_selenium_install(
            args,
            logger,
            jar_name,
            url_base,
            config_src,
            config_dst
        )
    elif args.start:
        handle_command_selenium_start(
            args,
            logger,
            jar_name,
            config_dst,
            drivers_abspaths
        )
    else:
        logger.error("ACTION not selected: --install , --start")

def handle_command_selenium_start(args, logger, selenium_jar,
                                  config_dst, drivers_abspaths):
    """TODO: doc method"""
    platforms = ["win32", "win64", "lin32", "lin64"]
    msgs_start = [
        "Can't start without select available platform: [win32,win64,lin32,lin64]"
    ]
    cmd_args = ["java"]
    cmd_drivers = []
    cmd_default_args = [
        "-jar", "{}/{}".format(PATH_SERVER_DRIVERS, selenium_jar),
        "-role", args.mode,
        "-{}Config".format(args.mode), config_dst,
        "-log", "logs/selenium.{}.log".format(args.mode)
    ]
    if (
            args.mode == 'node' and
            (
                args.platform is None or
                args.platform not in platforms
            )
        ):
        logger.error(msgs_start[0])
        return
    elif args.platform == "win32":
        cmd_drivers.extend(name_filter_win32(drivers_abspaths))
    elif args.platform == "win64":
        cmd_drivers.extend(name_filter_win64(drivers_abspaths))
    elif args.platform == "lin32":
        cmd_drivers.extend(name_filter_lin32(drivers_abspaths))
    elif args.platform == "lin64":
        cmd_drivers.extend(name_filter_lin64(drivers_abspaths))
    if args.mode == "node":
        cmd_args.extend(cmd_drivers)
    cmd_args.extend(cmd_default_args)
    logger.info("Executing command : {}".format(cmd_args))
    return subprocess.call(cmd_args)

def handle_command_selenium_install(args, logger, selenium_jar,
                                    selenium_url, config_src, config_dst):
    """TODO: doc method"""
    msgs_install = [
        "Installation : {}, copying configuration file from example",
        "Selenium JAR ready at: {}",
        "Downloading selenium from : {}",
        "Installation : drivers ready at path, modules/qadrivers",
        "Installation : COMPLETED"
        ]
    jar_path = "{}/{}".format(PATH_SERVER_DRIVERS, selenium_jar)
    if os.path.exists(jar_path):
        logger.info(msgs_install[0].format(jar_path))
    else:
        logger.info(msgs_install[1].format(selenium_url))
        wget.download(selenium_url, out=PATH_SERVER_DRIVERS)
    logger.info(msgs_install[2].format(args.mode))
    shutil.copy2(config_src, config_dst)
    logger.info(msgs_install[3])
    logger.info(msgs_install[4])


def name_filter_lin64(drivers_abspaths):
    """Return array ofparsed absolute paths name for platform LINUX 64"""
    return [
        name_filter(drivers_abspaths, "chromedriver_64"),
        name_filter(drivers_abspaths, "firefoxdriver_64"),
        name_filter(drivers_abspaths, "phantomjsdriver_64")
    ]

def name_filter_lin32(drivers_abspaths):
    """Return array ofparsed absolute paths name for platform LINUX 32"""
    return [
        name_filter(drivers_abspaths, "chromedriver_32"),
        name_filter(drivers_abspaths, "firefoxdriver_32"),
        name_filter(drivers_abspaths, "phantomjsdriver_32")
    ]

def name_filter_win64(drivers_abspaths):
    """Return array ofparsed absolute paths name for platform WINDOWS 64"""
    return [
        name_filter(drivers_abspaths, "chromedriver_32.exe"),
        name_filter(drivers_abspaths, "firefoxdriver_64.exe"),
        name_filter(drivers_abspaths, "phantomjsdriver_64.exe"),
        name_filter(drivers_abspaths, "iexplorerdriver_64.exe"),
        name_filter(drivers_abspaths, "edgedriver_64.exe")]

def name_filter_win32(drivers_abspaths):
    """Return array ofparsed absolute paths name for platform WINDOWS 32"""
    return [
        name_filter(drivers_abspaths, "chromedriver_32.exe"),
        name_filter(drivers_abspaths, "firefoxdriver_32.exe"),
        name_filter(drivers_abspaths, "phantomjsdriver_32.exe"),
        name_filter(drivers_abspaths, "iexplorerdriver_32.exe")
    ]

def name_filter(names=None, endswith=""):
    """Filter for name ending with text filter"""
    names = list(names)
    for name in names:
        if name.endswith(endswith):
            return name

def get_driver_abspath(driver_var, driver_path, driver_name):
    """Concatenate path name + driver name"""
    return "{}{}{}".format(driver_var, driver_path, driver_name)

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
