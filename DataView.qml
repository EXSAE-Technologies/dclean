//import related modules
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import Models

Component {
    id: pandas

    TableView {
        anchors.fill: parent
        columnSpacing: 1
        rowSpacing: 1
        clip: true

        model: pandasModel
    }

    PandasModel {
        id:pandasModel
    }
}