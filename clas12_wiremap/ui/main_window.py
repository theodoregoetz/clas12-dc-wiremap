from __future__ import print_function, division

import os

from clas12_wiremap.ui import QtGui, uic
from clas12_wiremap.ui import Sidebar, CrateTab, DBTab, TBTab, WireMap

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        curdir = os.path.dirname(os.path.realpath(__file__))
        uic.loadUi(os.path.join(curdir,'MainWindow.ui'), self)

        self.sidebar = Sidebar()
        sidebar_vbox = QtGui.QVBoxLayout()
        sidebar_vbox.addWidget(self.sidebar)
        sidebar_vbox.addStretch(1)
        self.sidebar_holder.setLayout(sidebar_vbox)

        self.crate = CrateTab()
        crate_vbox = QtGui.QVBoxLayout()
        crate_vbox.addWidget(self.crate)
        crate_vbox.addStretch(1)
        self.crate_tab_holder.setLayout(crate_vbox)

        self.dboard = DBTab()
        dboard_vbox = QtGui.QVBoxLayout()
        dboard_vbox.addWidget(self.dboard)
        dboard_vbox.addStretch(1)
        self.distr_board_tab_holder.setLayout(dboard_vbox)

        self.tboard = TBTab()
        tboard_vbox = QtGui.QVBoxLayout()
        tboard_vbox.addWidget(self.tboard)
        tboard_vbox.addStretch(1)
        self.trans_board_tab_holder.setLayout(tboard_vbox)

        self.wire_map = WireMap()
        wmap_vbox = QtGui.QVBoxLayout()
        wmap_vbox.addWidget(self.wire_map)
        self.wire_map_tab_holder.setLayout(wmap_vbox)

        self.show()
        self.updating = False

    def update_parameters(self):
        if not self.updating:
            self.updating = True
            self.updating = False

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
