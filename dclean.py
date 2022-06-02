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

       # Menus
       self.file_menu = self.menuBar().addMenu("File")
       self.setFileMenuActions()

       self.home_menu = self.menuBar().addMenu("Home")
       self.setHomeMenuActions()

       # Stack widget as central widget
       stack = QStackedWidget()
       self.setCentralWidget(stack)

       # Home page UI
       self.homePage = HomePage()
       stack.addWidget(self.homePage)

       # Load the plugins
       self.loadPlugins()
    
    # Menu actions
    def setFileMenuActions(self):
       # Exit QAction
       exit_action = QAction("Exit", self)
       exit_action.setShortcut(QKeySequence.Quit)
       exit_action.triggered.connect(self.close)
       self.file_menu.addAction(exit_action)
    
    def setHomeMenuActions(self):
       # Dashboard QAction
       dashboard_action = QAction("Dashboard", self)
       dashboard_action.triggered.connect(lambda: self.centralWidget().setCurrentIndex(0))
       self.home_menu.addAction(dashboard_action)
    
    def loadPlugins(self):
        for plugin in config.PLUGINS:
            a:QWidget = plugin.main()
            self.centralWidget().addWidget(a)
            a.index = self.centralWidget().indexOf(a)

            if callable(getattr(a,'setMenus',None)):
                a.setMenus(self.menuBar())
            
            if callable(getattr(a,'setHomePageUI',None)):
                a.setHomePageUI(self.homePage.layout())
            
            if callable(getattr(a,'setFileMenuActions',None)):
                a.setFileMenuActions(self.file_menu)
            
            if callable(getattr(a,'setHomeMenuActions',None)):
                a.setHomeMenuActions(self.home_menu)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()