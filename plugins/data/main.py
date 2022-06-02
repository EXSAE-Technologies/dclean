from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableView,
    QMenuBar,
    QMenu,
    QFileDialog
)
from PySide6.QtGui import (
    QAction,
)
from PySide6.QtCore import (
    QUrl
)
import pandas

from plugins.data.models import PandasModel

class DataPage(QWidget):
    def __init__(self,*args,**kwargs):
        QWidget.__init__(self)

        self.index = None

        # Layout
        pageLayout = QVBoxLayout()
        self.setLayout(pageLayout)

        # Table view
        self.table = QTableView()
        self.table.horizontalHeader().setStretchLastSection(True)
        pageLayout.addWidget(self.table)
    
    def setMenus(self,menuBar: QMenuBar):
        data_menu = menuBar.addMenu("Data")

        viewer_action = data_menu.addAction("Data Viewer")
        viewer_action.triggered.connect(lambda: self.parent().setCurrentIndex(self.index))
        
        import_menu = QMenu("Import")
        data_menu.addMenu(import_menu)
        import_csv_action = import_menu.addAction("CSV")
        import_csv_action.triggered.connect(self.import_csv_dialog)
    
    def import_csv_dialog(self):
        file = QFileDialog.getOpenFileUrl(self,"Import","/home","(*.csv)")
        if not file[0].isEmpty():
            df = pandas.read_csv(file[0].toLocalFile())
            model = PandasModel(df)
            self.table.setModel(model)
            if self.parent().currentIndex() != self.index:
                self.parent().setCurrentIndex(self.index)
