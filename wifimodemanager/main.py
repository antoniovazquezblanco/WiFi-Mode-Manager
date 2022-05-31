#!/usr/bin/env python

'''
Program entry point. Just instantiates the main window and launches a PySide
application to show it.
'''

import sys
from PySide2.QtWidgets import QApplication
from wifimodemanager.ui.window.wifi_mode_manager_window import (
    WifiModeManagerWindow
)


def main():
    '''
    Application entry point. Instantiates the PySide application and shows the
    main window.
    '''
    app = QApplication()
    wmm_window = WifiModeManagerWindow()
    wmm_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
