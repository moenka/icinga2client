#!/usr/bin/env python3
""" icinga2client """

from argparse import ArgumentDefaultsHelpFormatter, \
                     ArgumentParser
import json
import os
import sys


HOME_DIR = os.environ['HOME']
DEFAULT_CONFIG_DIR = '%s/.config/icinga2client/config.ini' % HOME_DIR
DEFAULT_HOST = 'http://localhost'
DEFAULT_PORT = '5665'


def run():
    parser = ArgumentParser(description=__doc__, prog='icinga2client',
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('-c', '--config',
                        type=str, default=DEFAULT_CONFIG_DIR,
                        help=('set configuration file'))
    parser.add_argument('-H', '--host',
                        type=str, default=DEFAULT_HOST,
                        help=('set api endpoint'))
    parser.add_argument('-p', '--port',
                        type=str, default=DEFAULT_PORT,
                        help=('set port of api endpoint'))
    parser.add_argument('-k', '--insecure',
                        type=bool, default=False, dest='insecure',
                        help=('ignore certificate warnings'))
    subparsers = parser.add_subparsers(metavar='COMMAND')

    # login
    p_login = subparsers.add_parser('login',
                                    help=('log into a icinga 2 api endpoint'))
    p_login.set_defaults(#todo)

    args = parser.parse_args()

    # action

    print('Hello World!')


if __name__ == '__main__':
    run()

# https://github.com/tobiasvdk/icinga2api

