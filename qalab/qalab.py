#! /usr/bin/env python
import argparse, logging, logging.handlers, os, shutil, sys, subprocess
import wget


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    logger = logging.getLogger('qalab')
    logger.setLevel(logging.DEBUG)
    if not os.path.exists('../logs'): os.mkdir('../logs')
    log_file_handler = logging.handlers.TimedRotatingFileHandler('../logs/qalab.log', when='M', interval=2)
    log_file_handler.setFormatter( logging.Formatter('%(asctime)s [%(levelname)s](%(name)s:%(funcName)s:%(lineno)d): %(message)s') )
    log_file_handler.setLevel(logging.DEBUG)
    logger.addHandler(log_file_handler)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.CRITICAL)
    console_handler.setFormatter( logging.Formatter('[%(levelname)s](%(name)s): %(message)s') )
    logger.addHandler(console_handler)

    parser = argparse.ArgumentParser(
        description="Performs selenium drivers operations",
        epilog="----- help us on , https://github.com/netzulo/qalab -------",
        fromfile_prefix_chars='@',)
    ## Main args
    parser.add_argument('-v', '--verbose', action="count", help="verbose level... repeat up to three times.")
    ## Args with subs
    commands = parser.add_subparsers(dest="selenium", help="Actions for selenium instance")
    command_install = commands.add_parser("selenium", help="Actions for selenium HUB or NODE")
    command_install.add_argument('-m','--mode', default=None, help="Select mode, values are: [hub, node]")
    command_install.add_argument('-i','--install', action="store_true", help="Download selenium jar")
    command_install.add_argument('-s','--start', action="store_true", help="Start Selenium jar")
    command_install.add_argument('-p','--platform', default=None, help="Select mode, values are: [lin32,lin64,win32,win64]")
    # START SCRIPT
    args = parser.parse_args()
    set_log_level_from_verbose(console_handler,args)

    if args.selenium == 'selenium':
        handle_command_selenium(args, logger)
    else:
        logger.error("Unknown command: {}".format(args))

def handle_command_selenium(args, logger):
    selenium_url_base = "https://selenium-release.storage.googleapis.com"
    selenium_url_version= "3.5"
    selenium_url_file = "3.5.3"
    selenium_jar = "selenium-server-standalone-{}.jar".format(selenium_url_file)
    selenium_url = "{}/{}/{}".format(selenium_url_base,
                                  selenium_url_version,
                                  selenium_jar)
    config_src = "qalab/configs/settings.{}.example.json".format(args.mode)
    config_dst = "qalab/configs/settings.{}.json".format(args.mode)
    platforms = ["win32", "win64","lin32","lin64"]
    drivers_path = "modules/qadrivers/"
    drivers_vars = ["-Dwebdriver.chrome.driver=","-Dwebdriver.gecko.driver=","-Dphantomjs.binary.path=",
                   "-Dwebdriver.ie.driver=", "-Dwebdriver.edge.driver="]
    drivers_names = ["chromedriver_32.exe", "chromedriver_64.exe","chromedriver_32","chromedriver_64",
                     "firefoxdriver_32.exe", "firefoxdriver_64.exe","firefoxdriver_32","firefoxdriver_64",
                     "phantomjsdriver_32.exe", "phantomjsdriver_64.exe","phantomjsdriver_32","phantomjsdriver_64",
                     "iexplorerdriver_32.exe","iexplorerdriver_64.exe",
                     "edgedriver_32.exe","edgedriver_64.exe"]
    drivers_abspaths = []
                
    for driver_name in drivers_names:
        if driver_name.startswith("chrome"):
            drivers_abspaths.append(get_driver_abspath(drivers_vars[0],drivers_path, driver_name))
        if driver_name.startswith("firefox"):
            drivers_abspaths.append(get_driver_abspath(drivers_vars[1],drivers_path, driver_name))
        if driver_name.startswith("phantomjs"):
            drivers_abspaths.append(get_driver_abspath(drivers_vars[2],drivers_path, driver_name))
        if driver_name.startswith("iexplorer"):
            drivers_abspaths.append(get_driver_abspath(drivers_vars[3],drivers_path, driver_name))
        if driver_name.startswith("edge"):
            drivers_abspaths.append(get_driver_abspath(drivers_vars[4],drivers_path, driver_name))

    if args.mode is None:
        logger.error("Can't start without select available mode: [hub, node]")
        return
    else:
        if args.install:
            jar_path = "{}/{}".format("qalab/drivers",selenium_jar)
            if os.path.exists(jar_path):
                logger.info("Selenium JAR ready at: {}".format(jar_path))
            else:
                logger.info("Downloading selenium from : {}".format(selenium_url))
                selenium_file = wget.download(selenium_url, out="qalab/drivers")
            logger.info("Installation : {}, copying configuration file from example".format(args.mode))
            shutil.copy2(config_src , config_dst)
            logger.info("Installation : drivers ready at path, modules/qadrivers")
            logger.info("Installacion : COMPLETED")
        elif args.start:
            cmd_args = ["java"]
            cmd_drivers = []
            cmd_default_args = ["-jar", "qalab/drivers/{}".format(selenium_jar),"-role", args.mode, "-{}Config".format(args.mode), config_dst,"-log","logs/selenium.{}.log".format(args.mode)]            

            if args.platform is None or args.platform not in platforms:
                logger.error("Can't start without select available platform: [win32,win64,lin32,lin64]")
                return
            elif args.platform == "win32":
                cmd_drivers.extend([name_filter(drivers_abspaths,"chromedriver_32.exe"),
                                    name_filter(drivers_abspaths,"firefoxdriver_32.exe"),
                                    name_filter(drivers_abspaths,"phantomjsdriver_32.exe"),
                                    name_filter(drivers_abspaths,"iexplorerdriver_32.exe")])
            elif args.platform == "win64":
                cmd_drivers.extend([name_filter(drivers_abspaths,"chromedriver_32.exe"),
                                    name_filter(drivers_abspaths,"firefoxdriver_64.exe"),
                                    name_filter(drivers_abspaths,"phantomjsdriver_64.exe"),
                                    name_filter(drivers_abspaths,"iexplorerdriver_64.exe"),
                                    name_filter(drivers_abspaths,"edgedriver_64.exe")])
            elif args.platform == "lin32":
                cmd_drivers.extend([name_filter(drivers_abspaths,"chromedriver_32"),
                                    name_filter(drivers_abspaths,"firefoxdriver_32"),
                                    name_filter(drivers_abspaths,"phantomjsdriver_32")])
            elif args.platform == "lin64":
                cmd_drivers.extend([name_filter(drivers_abspaths,"chromedriver_64"),
                                    name_filter(drivers_abspaths,"firefoxdriver_64"),
                                    name_filter(drivers_abspaths,"phantomjsdriver_64")])

            if args.mode == "node":
                cmd_args.extend(cmd_drivers)
            cmd_args.extend(cmd_default_args)
            logger.info("Executing command : {}".format(cmd_args))
            subprocess.call(cmd_args)
            pass
        else:
            logger.error("ACTION not selected: --install , --start")

def name_filter(names=[], endswith=""):
    for name in names:
        if name.endswith(endswith):
            return name

def get_driver_abspath(driver_var, driver_path, driver_name):
    return "{}{}{}".format(driver_var, driver_path, driver_name)

def set_log_level_from_verbose(console_handler, args):
    if not args.verbose:
        console_handler.setLevel("INFO")
    elif args.verbose == 1:
        console_handler.setLevel('WARNING')
    elif args.verbose == 2:
        console_handler.setLevel('INFO')
    elif args.verbose >= 3:
        console_handler.setLevel('DEBUG')
    else:
        logger.critical("LOGGER leve doesn't exist")


if __name__ == '__main__':
    main()
