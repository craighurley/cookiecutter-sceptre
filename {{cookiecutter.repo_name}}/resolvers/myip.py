#!/usr/bin/env python

import ipaddress
import os
import sys
import requests
from sceptre.resolvers import Resolver

class MyIp(Resolver):
    """
    Get the public IP address of the caller.
    """

    def __init__(self, *args, **kwargs):
        super(MyIp, self).__init__(*args, **kwargs)

    def resolve(self):
        try:
            ip = requests.get('http://checkip.amazonaws.com/').text.replace('\r', '').replace('\n', '')
        except requests.RequestException:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('Error performing GET on the checkip service; file: %s, line: %s' % (fname, exc_tb.tb_lineno))
            sys.exit(1)

        try:
            ip_address = ipaddress.ip_address(ip)
        except ValueError:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('Invalid response from checkip service; file: %s, line: %s' % (fname, exc_tb.tb_lineno))
            sys.exit(1)

        return ip + '/32'
