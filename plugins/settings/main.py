from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QMenuBar,
    QGridLayout,
)
from PySide6.QtGui import (
    QAction,
    QKeySequence
)

class SettingsPage(QWidget):
    def __init__(self,*args,**kwargs):
        QWidget.__init__(self)

        self.index = None

        # Layout
        pageLayout = QVBoxLayout()
        self.setLayout(pageLayout)

        # Initialize the layout
        self.setUI()
    
    def setMenus(self,menuBar: QMenuBar):
        settings_menu = menuBar.addMenu("Settings")

        general_action = QAction("General", self)
        general_action.triggered.connect(self.on_general_action)
        settings_menu.addAction(general_action)
    
    def on_general_action(self):
        self.parent().setCurrentIndex(self.index)
    
    def setUI(self):
        words = QLabel(text="Hello Settings")
        self.layout().addWidget(words)
    
    def setHomePageUI(self,layout: QGridLayout):
        words = QLabel(text="Hello World")
        layout.addWidget(words)
