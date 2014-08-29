#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 Mitchell Chu

from driver import SessionDriver
# from session import SessionConfigurationError
import memcache
import datetime
import numbers
from copy import copy
try:
    import cPickle as pickle    # py2
except:
    import pickle               # py3

"""
NOTICE:
This session extension was not be tested.
you must test all functions before use.
"""

class MemcachedSession(SessionDriver):
    """
    Use memcached to save session object
    """
    DEFAULT_MEMCACHED_HOST = '127.0.0.1'
    DEFAULT_MEMCACHED_PORT = '11211'

    def __init__(self, **settings):
        super(MemcachedSession, self).__init__(**settings)
        self.client = self.__create_memcached_client()

    def get(self, session_id):
        mem_data = self.client.get(session_id)
        if not mem_data: return {}
        return pickle.loads(mem_data)

    def save(self, session_id, session_data, expires=None):
        session_data = session_data if session_data else {}
        if expires:
            session_data.update(__expires__ = expires)
        mem_data = pickle.dumps(session_data)
        expires = self.__get_expires_seconds(expires)
        self.client.set(session_id, mem_data, expires)

    def clear(self, session_id):
        self.client.delete(session_id)

    def remove_expires(self):
        pass

    def __create_memcached_client(self):
        settings = copy(self.settings)
        host = settings.pop('host', self.DEFAULT_MEMCACHED_HOST)
        port = settings.pop('port', self.DEFAULT_MEMCACHED_PORT)
        servers = '%s:%s' % (host, port)
        return memcache.Client(servers, **settings)
            
    def __get_expires_seconds(self, expires):
        if isinstance(expires, numbers.Real):
            return int(expires)
        elif isinstance(expires, datetime.datetime):
            now = datetime.datetime.utcnow()
            return int((expires - now).total_seconds())
        else:
            return 0
