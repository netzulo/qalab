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
from qalab.core.server_driver_selenium import ServerDriverSelenium
import wget


# SETTINGS start
PATH_CONFIG = 'qalab/configs'
PATH_DRIVERS_MODULE = 'modules/qadrivers/'
PATH_SERVER_DRIVERS = 'qalab/drivers'
PATH_APKS = 'qalab/apks'
WEBDRIVER_ENV_VARS = [
    "-Dwebdriver.chrome.driver=",
    "-Dwebdriver.gecko.driver=",
    "-Dphantomjs.binary.path=",
    "-Dwebdriver.ie.driver=",
    "-Dwebdriver.edge.driver=",
    "-Dwebdriver.opera.driver="
]
DRIVERS_NAMES = [
    "chromedriver_32.exe",
    "chromedriver_64.exe",
    "chromedriver_32",
    "chromedriver_64",
    "firefoxdriver_32.exe",
    "firefoxdriver_64.exe",
    "firefoxdriver_32",
    "firefoxdriver_64",
    "phantomjsdriver_32.exe",
    "phantomjsdriver_64.exe",
    "phantomjsdriver_32",
    "phantomjsdriver_64",
    "iexplorerdriver_32.exe",
    "iexplorerdriver_64.exe",
    "edgedriver_32.exe",
    "edgedriver_64.exe",
    "operadriver_32.exe",
    "operadriver_64.exe",
    "operadriver_32",
    "operadriver_64",
]
MSG_UNKOWN_COMMAND = "Unknown command : {}"
### COMMON
# {path}/{args.server_driver}.{args.mode}.json
DRIVER_CONFIG_PATH = "{}/{}.{}.json"
# {path}/{args.server_driver}.{args.mode}.example.json
DRIVER_CONFIG_PATH_EXAMPLE = "{}/{}.{}.example.json"
### SELENIUM
SELENIUM_VERSION = "3.5"
SELENIUM_VERSION_BUILD = "3.5.3"
SELENIUM_JAR_NAME = "selenium-server-standalone-{}.jar".format(
    SELENIUM_VERSION_BUILD)
SELENIUM_URL = "https://selenium-release.storage.googleapis.com/{}/{}".format(
    SELENIUM_VERSION, SELENIUM_JAR_NAME)

### SELENDROID
# Selendroid , TODO: just for mode node
SELENDROID_PORT = 12000
SELENDROID_SELENDROID_VERSION = '0.17.0'
SELENDROID_JAR = 'selendroid-standalone-{}-with-dependencies.jar'.format(
    SELENDROID_SELENDROID_VERSION)
SELENDROID_URL = '{}/{}/{}'.format(
    'https://github.com/selendroid/selendroid/releases/download',
    SELENDROID_SELENDROID_VERSION,
    SELENDROID_JAR)
# Selendroid plugin, TODO: just for mode node
SELENDROID_PLUGIN_JAR = 'selendroid-grid-plugin-{}.jar'.format(
    SELENDROID_SELENDROID_VERSION)
SELENDROID_PLUGIN_URL = '{}/{}/{}'.format(
    'http://search.maven.org/remotecontent?filepath=io/selendroid/selendroid-grid-plugin',
    SELENDROID_SELENDROID_VERSION,
    SELENDROID_JAR)
# Selenium, TODO: just for mode hub
SELENDROID_SELENIUM_VERSION = "3.5.3"
SELENDROID_SELENIUM_JAR = "selenium-server-standalone-{}.jar".format(
    SELENDROID_SELENIUM_VERSION)
SELENDROID_SELENIUM_URL = "https://selenium-release.storage.googleapis.com/3.5/{}".format(
    SELENDROID_SELENIUM_JAR)
# SETTINGS end


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
    #TODO, que esto funcion -> server_driver = ServerDriverSelenium(args.mode)
    # required --mode param
    if args.mode not in ['hub', 'node']:
        raise Exception('Select valid mode, values are: [hub, node]')
    config_src = DRIVER_CONFIG_PATH_EXAMPLE.format(
        PATH_CONFIG, 'selenium', args.mode)
    config_dst = DRIVER_CONFIG_PATH.format(
        PATH_CONFIG, 'selenium', args.mode)
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
        if driver_name.startswith("opera"):
            webdriver_var_name = WEBDRIVER_ENV_VARS[5]
        # Get absolute path for driver_name
        drivers_abspaths.append(get_driver_abspath(
            webdriver_var_name, PATH_DRIVERS_MODULE, driver_name))

    if args.install:
        command_install(
            args, logger, SELENIUM_URL, SELENIUM_JAR_NAME, config_src, config_dst)
    elif args.start:
        handle_command_start_selenium(
            args, logger, SELENIUM_JAR_NAME, config_dst, drivers_abspaths)
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

def download_file(logger, url, out_path):
    """TODO: doc method"""
    logger.info('Downloading file: ...')
    logger.debug('  url={}'.format(url))
    logger.debug('  out_path={}'.format(out_path))
    wget.download(url, out=out_path)
    logger.info('Downloading file: DONE')

def copy_config(logger, config_src, config_dst):
    """TODO: doc method"""
    logger.info('Copy config: ...')
    logger.debug('  from={}'.format(config_src))
    logger.debug('  to={}'.format(config_dst))
    shutil.copy2(config_src, config_dst)
    logger.info('Copy config: DONE')

def handle_command_start_selenium(args, logger, selenium_jar,
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

def name_filter_lin64(drivers_abspaths):
    """Return array ofparsed absolute paths name for platform LINUX 64"""
    return [
        name_filter(drivers_abspaths, "chromedriver_64"),
        name_filter(drivers_abspaths, "firefoxdriver_64"),
        name_filter(drivers_abspaths, "phantomjsdriver_64"),
        name_filter(drivers_abspaths, "operadriver_64")
    ]

def name_filter_lin32(drivers_abspaths):
    """Return array ofparsed absolute paths name for platform LINUX 32"""
    return [
        name_filter(drivers_abspaths, "chromedriver_32"),
        name_filter(drivers_abspaths, "firefoxdriver_32"),
        name_filter(drivers_abspaths, "phantomjsdriver_32"),
        name_filter(drivers_abspaths, "operadriver_32")
    ]

def name_filter_win64(drivers_abspaths):
    """Return array ofparsed absolute paths name for platform WINDOWS 64"""
    return [
        name_filter(drivers_abspaths, "chromedriver_32.exe"),
        name_filter(drivers_abspaths, "firefoxdriver_64.exe"),
        name_filter(drivers_abspaths, "phantomjsdriver_64.exe"),
        name_filter(drivers_abspaths, "iexplorerdriver_64.exe"),
        name_filter(drivers_abspaths, "edgedriver_64.exe"),
        name_filter(drivers_abspaths, "operadriver_64.exe")
    ]

def name_filter_win32(drivers_abspaths):
    """Return array ofparsed absolute paths name for platform WINDOWS 32"""
    return [
        name_filter(drivers_abspaths, "chromedriver_32.exe"),
        name_filter(drivers_abspaths, "firefoxdriver_32.exe"),
        name_filter(drivers_abspaths, "phantomjsdriver_32.exe"),
        name_filter(drivers_abspaths, "iexplorerdriver_32.exe"),
        name_filter(drivers_abspaths, "operadriver_32.exe")
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
