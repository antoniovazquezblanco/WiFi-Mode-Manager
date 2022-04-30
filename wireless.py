#!/usr/bin/env python

'''
Helper functions that interface with iw.
'''

from pyric import pyw


def get_wireless_interfaces():
    '''
    Get wireless interfaces information
    '''
    devs = pyw.winterfaces()
    cards = [pyw.getcard(x) for x in devs]
    wireless_interfaces = [
        {
            'dev': x.dev,
            'chipset': pyw.ifinfo(x)['chipset'],
            'mode': pyw.devinfo(x)['mode']
        }
        for x in cards
    ]
    return wireless_interfaces
