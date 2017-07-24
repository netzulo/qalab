#! /usr/bin/env python
import argparse, logging, logging.handlers, os, wget

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
    fromfile_prefix_chars='@',
)
## Main args
parser.add_argument('-v', '--verbose', action="count", help="verbose level... repeat up to three times.")
## Args with subs
commands = parser.add_subparsers(dest='install', help="Install command")
command_install = commands.add_parser("install", help="Install selenium HUB or NODE")
command_install.add_argument('--hub', default=None, help="Install selenium hub", metavar="VERSION")
command_install.add_argument('--node', default=None, help="Install selenium node", metavar="VERSION")


def handle_command_install(args):
    logger.error("handled command: install, with args={}".format(args))

    selenium_url_base = "https://selenium-release.storage.googleapis.com"
    selenium_url_version= "3.4"
    selenium_url_file = "3.4.0"
    selenium_jar = "selenium-server-standalone-{}.jar".format(selenium_url_file)
    selenium_url = "{}/{}/{}".format(selenium_url_base,
                                  selenium_url_version,
                                  selenium_jar)
    if args.hub is not None:
        logger.error("HUB install detected")
    if args.node is not None:
        logger.error("NODE install detected")

    logger.error("Downloading selenium from : {}".format(selenium_url))
    selenium_file = wget.download(selenium_url)

    logger.error("PROCESS NOT IMPLEMENTED")


def set_log_level_from_verbose(args):
    if not args.verbose:
        console_handler.setLevel('ERROR')
    elif args.verbose == 1:
        console_handler.setLevel('WARNING')
    elif args.verbose == 2:
        console_handler.setLevel('INFO')
    elif args.verbose >= 3:
        console_handler.setLevel('DEBUG')
    else:
        logger.critical("LOGGER leve doesn't exist")


if __name__ == '__main__':
    args = parser.parse_args()
    set_log_level_from_verbose(args)
    if args.install == 'install':
        handle_command_install(args)    
    else:
        logger.error("Unknown command: {}".format(args.install))