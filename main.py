#!/usr/bin/env python

'''
Program entry point. Just instaniates the main window and launches a PySide app
to show it.
'''

import sys
from PySide2.QtWidgets import QApplication
from ui.window.wifi_mode_manager_window import WifiModeManagerWindow


if __name__ == "__main__":
    app = QApplication()
    wmm_window = WifiModeManagerWindow()
    wmm_window.show()
    sys.exit(app.exec_())
