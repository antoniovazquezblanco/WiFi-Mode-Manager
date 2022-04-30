#!/usr/bin/env python

'''
Helper functions that interface with iw. It also supports udev interaction for
async events.
'''

import pyudev
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

class WirelessUdevObserver():
    def __init__(self):
        context = pyudev.Context()
        monitor = pyudev.Monitor.from_netlink(context)
        monitor.filter_by(subsystem='net', device_type='wlan')
        self._observer = pyudev.MonitorObserver(monitor, self._event)
        self._observer.start()
        self._callbacks = []

    def stop(self):
        self._observer.stop()

    def suscribe(self, callback):
        self._callbacks.append(callback)

    def _event(self, action, device):
        for cb in self._callbacks:
            cb()
