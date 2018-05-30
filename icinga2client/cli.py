#!/usr/bin/env python3
''' icinga2client '''

from argparse import ArgumentDefaultsHelpFormatter, \
                     ArgumentParser
from icinga2client.client import Client
import json
import os
import sys
import ui
import urllib3


def run():
    parser = ArgumentParser(description=__doc__, prog='icinga2client',
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('-A', '--attrs',
                        type=str, default='{}',
                        help=('Set the attributes of an object in JSON format'))
    parser.add_argument('-H', '--host',
                        type=str, default='https://localhost',
                        help=('Set host of api server'))
    parser.add_argument('-p', '--password',
                        type=str, default='director',
                        help=('Set passwort of the API user'))
    parser.add_argument('-P', '--port',
                        type=str, default='5665',
                        help=('Set port of api server'))
    parser.add_argument('-r', '--raw',
                        action='store_true',
                        help=('Print raw output instead of json'))
    parser.add_argument('-R', '--recursive',
                        action='store_true',
                        help=('Recursively run command on all child objects.'))
    parser.add_argument('-t', '--template',
                        type=str, default='generic-host',
                        help=('Set template to use for object creation'))
    parser.add_argument('-u', '--username',
                        type=str, default='director',
                        help=('Set username of the API user'))
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help=('Show more verbose output'))
    parser.add_argument('command',
                        choices=[
                            'show',
                            'create',
                            'update',
                            'delete'
                        ],
                        help=('Run a command on an object'))
    parser.add_argument('type',
                        choices=[
                            'Host',
                            'Service'
                        ],
                        help=('Set the object type'))
    parser.add_argument('name',
                        type=str, metavar='NAME',
                        help=('The name of the object, use \'all\' to run the command on all '
                              'objects of a specific type'))
    args = parser.parse_args()

    if args.verbose is True:
        ui.debug(args)
    else:
        urllib3.disable_warnings()

    client = Client(args)
    getattr(client, args.command)(args)


if __name__ == '__main__':
    run()

