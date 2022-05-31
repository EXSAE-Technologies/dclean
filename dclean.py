import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import Signal, Slot, QObject
from PySide6.QtQml import QQmlApplicationEngine, QmlElement
from PySide6.QtQuickControls2 import QQuickStyle

import style_rc
from models import PandasModel

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    QQuickStyle.setStyle("Material")
    engine = QQmlApplicationEngine()
    engine.load('view.qml')
    
    if not engine.rootObjects():
        sys.exit(-1)
    
    sys.exit(app.exec())