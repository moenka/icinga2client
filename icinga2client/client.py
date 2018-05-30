''' i2c/client.py '''

from icinga2api.client import Client as APIClient
from icinga2api.exceptions import Icinga2ApiException
from requests.exceptions import ConnectionError
import json
import ui
import sys


class Client(object):

  client = None
  raw = False
  verbose = False

  def __init__(self, args):
    url = '%s:%s' % (args.host, args.port)
    self.client = APIClient(url, args.username, args.password)
    self.raw = args.raw
    self.verbose = args.verbose
    ui.setup(verbose=args.verbose)

  def __output(self, obj):
    if self.raw:
      print(obj)
    else:
      print(json.dumps(obj))

  def show(self, args):
    if args.name == 'all':
      self.__output(self.client.objects.list(args.type))
    else:
      try:
        self.__output(self.client.objects.get(args.type, args.name))
      except Icinga2ApiException as e:
        ui.debug(e)
        ui.fatal('No objects found.')

  def create(self, args):
    try:
      res = self.client.objects.create(
        args.type, args.name, [args.template], json.loads(args.attrs))
      self.__output(res)
    except Icinga2ApiException as e:
      ui.debug(e)
      ui.fatal('Object cannot be created because it already exists.')

  def update(self, args):
    if args.attrs == '{}':
      ui.warning('Empty attributes. Nothing to update.')
    else:
      attrs = {'attrs': json.loads(args.attrs)}
      self.__output(self.client.objects.update(args.type, args.name, attrs))

  def delete(self, args):
    try:
      res = self.client.objects.delete(args.type, args.name, cascade=args.recursive)
      self.__output(res)
    except Icinga2ApiException as e:
      ui.debug(e)
      ui.fatal('Object cannot be deleted because it was not created using the API.')

