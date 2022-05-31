from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)

class SettingsPage(QWidget):
    def __init__(self,*args,**kwargs):
        QWidget.__init__(self)

        # Layout
        self.pageLayout = QVBoxLayout()
        self.setLayout(self.pageLayout)

        # Initialize the layout
        self.setUI()
    
    def setMenus(self):
        file_menu = self.parent().parent().menuBar().addMenu("Settings")
    
    def setUI(self):
        words = QLabel(text="Hello World")
        self.pageLayout.addWidget(words)
