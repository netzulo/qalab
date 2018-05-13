# -*- coding: utf-8 -*-
"""Configuration settings for differents driver classes"""


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
# COMMON
# {path}/{args.server_driver}.{args.mode}.json
DRIVER_CONFIG_PATH = "{}/{}.{}.json"
# {path}/{args.server_driver}.{args.mode}.example.json
DRIVER_CONFIG_PATH_EXAMPLE = "{}/{}.{}.example.json"
# SELENIUM
MSG_PLATFORM_ERROR = "Can't without available platform: {}".format(
    "[win32,win64,lin32,lin64]")
SELENIUM_VERSION = "3.12"
SELENIUM_VERSION_BUILD = "3.12.0"
SELENIUM_JAR_NAME = "selenium-server-standalone-{}.jar".format(
    SELENIUM_VERSION_BUILD)
SELENIUM_URL = "https://selenium-release.storage.googleapis.com/{}/{}".format(
    SELENIUM_VERSION, SELENIUM_JAR_NAME)
