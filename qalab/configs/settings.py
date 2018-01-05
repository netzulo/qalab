# -*- coding: utf-8 -*-
"""TODO: doc module"""


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