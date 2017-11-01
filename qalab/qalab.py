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


def main(args=None):
    """TODO: doc method"""
    msg_unkown_command = "Unknown command : {}"
    msg_file_formatter = "{} [{}]({}:{}:{}): {}".format(
        "%(asctime)s",
        "%(levelname)s",
        "%(name)s",
        "%(funcName)s",
        "%(lineno)d",
        "%(message)s"
    )
    msg_console_formatter = '[%(levelname)s](%(name)s): %(message)s'
    if args is None:
        args = sys.argv[1:]
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
    ## Generate parser
    parser = argparse.ArgumentParser(
        description="Performs selenium drivers operations",
        epilog="----- help us on , https://github.com/netzulo/qalab -------",
        fromfile_prefix_chars='@',)
    ## Main args
    parser.add_argument(
        '-v', '--verbose',
        action="count", help="verbose level... repeat up to three times.")
    ## Args with subs
    commands = parser.add_subparsers(
        dest="selenium", help="Actions for selenium instance")
    command_install = commands.add_parser(
        "selenium", help="Actions for selenium HUB or NODE")
    command_install.add_argument(
        '-m', '--mode',
        default=None, help="Select mode, values are: [hub, node]")
    command_install.add_argument(
        '-i', '--install',
        action="store_true", help="Download selenium jar")
    command_install.add_argument(
        '-s', '--start',
        action="store_true", help="Start Selenium jar")
    command_install.add_argument(
        '-p', '--platform',
        default=None, help="Select mode, values are: [lin32,lin64,win32,win64]")
    args = parser.parse_args()
    set_log_level_from_verbose(console_handler, args, logger)
    # START SCRIPT
    if args.selenium == 'selenium':
        handle_command_selenium(args, logger)
    else:
        logger.error(str(msg_unkown_command.format(args)))

def handle_command_selenium(args, logger):
    """Command Selenium"""
    selenium_url_base = "https://selenium-release.storage.googleapis.com"
    selenium_url_version = "3.5"
    selenium_url_file = "3.5.3"
    selenium_jar = "selenium-server-standalone-{}.jar".format(selenium_url_file)
    selenium_url = "{}/{}/{}".format(
        selenium_url_base, selenium_url_version, selenium_jar)
    if args.mode not in ['hub', 'node']:
        raise Exception('Select valid mode, values are: [hub, node]')
    config_src = "qalab/configs/settings.{}.example.json".format(args.mode)
    config_dst = "qalab/configs/settings.{}.json".format(args.mode)
    platforms = ["win32", "win64", "lin32", "lin64"]
    drivers_path = "modules/qadrivers/"
    drivers_vars = [
        "-Dwebdriver.chrome.driver=",
        "-Dwebdriver.gecko.driver=",
        "-Dphantomjs.binary.path=",
        "-Dwebdriver.ie.driver=",
        "-Dwebdriver.edge.driver="
    ]
    drivers_names = [
        "chromedriver_32.exe", "chromedriver_64.exe",
        "chromedriver_32", "chromedriver_64",
        "firefoxdriver_32.exe", "firefoxdriver_64.exe",
        "firefoxdriver_32", "firefoxdriver_64",
        "phantomjsdriver_32.exe", "phantomjsdriver_64.exe",
        "phantomjsdriver_32", "phantomjsdriver_64",
        "iexplorerdriver_32.exe", "iexplorerdriver_64.exe",
        "edgedriver_32.exe", "edgedriver_64.exe"
    ]
    drivers_abspaths = []
    for driver_name in drivers_names:
        if driver_name.startswith("chrome"):
            drivers_abspaths.append(
                get_driver_abspath(
                    drivers_vars[0], drivers_path, driver_name))
        if driver_name.startswith("firefox"):
            drivers_abspaths.append(
                get_driver_abspath(
                    drivers_vars[1], drivers_path, driver_name))
        if driver_name.startswith("phantomjs"):
            drivers_abspaths.append(
                get_driver_abspath(
                    drivers_vars[2], drivers_path, driver_name))
        if driver_name.startswith("iexplorer"):
            drivers_abspaths.append(
                get_driver_abspath(
                    drivers_vars[3], drivers_path, driver_name))
        if driver_name.startswith("edge"):
            drivers_abspaths.append(
                get_driver_abspath(
                    drivers_vars[4], drivers_path, driver_name))
    if args.mode is None:
        logger.error("Can't start without select available mode: [hub, node]")
        return
    else:
        if args.install:
            msgs_install = [
                "Installation : {}, copying configuration file from example",
                "Selenium JAR ready at: {}",
                "Downloading selenium from : {}",
                "Installation : drivers ready at path, modules/qadrivers",
                "Installation : COMPLETED"
            ]
            jar_path = "{}/{}".format("qalab/drivers", selenium_jar)
            if os.path.exists(jar_path):
                logger.info(msgs_install[0].format(jar_path))
            else:
                logger.info(msgs_install[1].format(selenium_url))
                wget.download(selenium_url, out="qalab/drivers")
            logger.info(msgs_install[2].format(args.mode))
            shutil.copy2(config_src, config_dst)
            logger.info(msgs_install[3])
            logger.info(msgs_install[4])
        elif args.start:
            msgs_start = [
                "Can't start without select available platform: [win32,win64,lin32,lin64]"
            ]
            cmd_args = ["java"]
            cmd_drivers = []
            cmd_default_args = [
                "-jar", "qalab/drivers/{}".format(selenium_jar),
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
        else:
            logger.error("ACTION not selected: --install , --start")

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
