import config
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QWidget,
    QGridLayout
)
from PySide6.QtCore import (
    QAbstractTableModel,
    Qt,
    QModelIndex,
)
from PySide6.QtGui import (
    QAction, QKeySequence
)
import sys

class HomePage(QWidget):
    def __init__(self,*args,**kwargs):
        QWidget.__init__(self)

        # Layout
        pageLayout = QGridLayout()
        self.setLayout(pageLayout)
        
class MainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
       super().__init__(*args,**kwargs)
       self.title = "DClean"
       self.resize(800,500)

       # Window dimensions
       geometry = self.screen().availableGeometry()
       self.resize(geometry.width() * 0.8, geometry.height() * 0.7)

       # Menu
       self.file_menu = self.menuBar().addMenu("File")

       # Exit QAction
       exit_action = QAction("Exit", self)
       exit_action.setShortcut(QKeySequence.Quit)
       exit_action.triggered.connect(self.close)
       self.file_menu.addAction(exit_action)

       # Stack widget as central widget
       stack = QStackedWidget()
       self.setCentralWidget(stack)

       # Home page UI
       self.homePage = HomePage()
       stack.addWidget(self.homePage)

       # Load the plugins
       self.loadPlugins()
    
    def loadPlugins(self):
        for plugin in config.PLUGINS:
            a = plugin.main()
            self.centralWidget().addWidget(a)

            if callable(getattr(a,'setMenus',None)):
                a.setMenus()
            
            if callable(getattr(a,'setHomePageUI',None)):
                a.setHomePageUI()

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()