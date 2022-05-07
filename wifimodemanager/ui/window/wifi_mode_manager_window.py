#!/usr/bin/env python

'''
Main program window. Loaded from a qt-designer ui file. Implements main logic
to handle ui signals.
'''

from wifimodemanager import wireless
from qtpy import uic
from PySide2 import QtWidgets
from wifimodemanager.ui.dialog.about_dialog import AboutDialog
from wifimodemanager.ui.model.wireless_list_model import WirelessListModel


class WifiModeManagerWindow(QtWidgets.QMainWindow):
    '''
    Main program window. Loaded from a qt-designer ui file. Implements main
    logic to handle ui signals.
    '''

    def __init__(self, parent=None):
        super(WifiModeManagerWindow, self).__init__(parent)
        uic.loadUi(uifile='wifimodemanager/ui/window/WifiModeManagerWindow.ui',
                   baseinstance=self)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionRefresh.triggered.connect(self.refresh_interfaces)
        self.wireless_list_model = WirelessListModel()
        self.treeView.setModel(self.wireless_list_model)
        self.wireless_observer = wireless.WirelessUdevObserver()
        self.wireless_observer.subscribe(self.refresh_interfaces)
        self.refresh_interfaces()

    def closeEvent(self, event):
        if self.wireless_observer:
            self.wireless_observer.stop()
        event.accept()

    def show_about(self):
        '''Show the about dialog.'''
        AboutDialog(self)

    def refresh_interfaces(self):
        '''Update the wireless interfaces table.'''
        self.statusbar.showMessage("Refreshing...")
        self.wireless_list_model.addItems(wireless.get_wireless_interfaces())
        self.statusbar.showMessage("")
