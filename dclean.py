import config
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget
)
from PySide6.QtCore import (
    QAbstractTableModel,
    Qt,
    QModelIndex
)
import sys

class MainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
       super().__init__(*args,**kwargs)
       self.title = "DClean"
       self.resize(800,500)

       self.stack = QStackedWidget()

       # Load the plugins
       self.loadPlugins()
    
    def loadPlugins(self):
        for plugin in config.PLUGINS:
            self.stack.addWidget(plugin.main())

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()