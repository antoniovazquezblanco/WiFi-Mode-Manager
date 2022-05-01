#!/usr/bin/env python

'''
A simple about dialog
'''

from qtpy import uic
from PySide2 import QtWidgets


class AboutDialog(QtWidgets.QDialog):
    '''
    A simple about dialog
    '''

    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)
        uic.loadUi('ui/dialog/AboutDialog.ui', self)
        self.exec_()
