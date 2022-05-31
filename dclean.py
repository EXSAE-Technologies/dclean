from PySide6.QtWidgets import QTableView, QApplication, QMainWindow
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
import sys

class MainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
       super().__init__(*args,**kwargs)
       self.title = "DClean"
       self.resize(800,500)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()