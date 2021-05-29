# Dependencies
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys

# Local Imports
from src.plant_metadata import Tray
from src.db_interface import get_trays, add_tray
from src.ui_elements import TableModel

DB_PATH = 'C:\\Users\\tjalw\\Documents\\GitHub\\PyNursery\\db'


trays = get_trays(DB_PATH)
trays = [x.to_qt_table() for x in trays]


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, data):
        super().__init__()

        self.table = QtWidgets.QTableView()

        self.model = TableModel(data)
        self.model.setHeaderData(0, Qt.Orientation.Horizontal, "Tray Type")
        self.model.setHeaderData(1, Qt.Orientation.Horizontal, "Capacity")
        self.model.setHeaderData(2, Qt.Orientation.Horizontal, "Footprint")
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow(trays)
window.show()
app.exec_()
