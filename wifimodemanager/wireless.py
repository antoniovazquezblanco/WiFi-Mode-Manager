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
    devices = pyw.winterfaces()
    cards = [pyw.getcard(x) for x in devices]
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
    '''
    Class to handle subscriptions to the udev device changes service.
    '''

    def __init__(self):
        context = pyudev.Context()
        monitor = pyudev.Monitor.from_netlink(context)
        monitor.filter_by(subsystem='net', device_type='wlan')
        self._observer = pyudev.MonitorObserver(monitor, self._event)
        self._observer.start()
        self._callbacks = []

    def stop(self):
        '''
        Stop the observer joining the underlaying thread.
        '''
        self._observer.stop()

    def subscribe(self, callback):
        '''
        Subscribe a callback function to the udev events.
        '''
        self._callbacks.append(callback)

    def _event(
        self,
        action,  # pylint: disable=unused-argument
        device  # pylint: disable=unused-argument
    ):
        for callback in self._callbacks:
            callback()
