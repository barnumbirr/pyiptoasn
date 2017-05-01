#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

class IPLookup(object):

    def __init__(self, base_url='https://api.iptoasn.com/v1/as/ip/'):
        self.base_url = base_url
        self.opener = urllib2.build_opener()
        self.opener.addheaders.append(('Content-Type', 'application/json'))
        self.opener.addheaders.append(('User-agent', 'pyiptoasn - python wrapper \
        around iptoasn.com (github.com/mrsmn/pyiptoasn)'))

    def _request_get(self, ip):
        response_url = self.base_url + ip
        response = self.opener.open(response_url)
        if response.getcode() != 200:
            return None
        response = json.loads(response.read())
        if response is None or response['announced'] is False:
            return None
        return response

    def lookup(self, param=None):
        data = self._request_get(ip=param)
        return data
