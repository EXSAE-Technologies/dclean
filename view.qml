//import related modules
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import Models 1.0

//window containing the application
ApplicationWindow {

    visible: true

    //title of the application
    title: qsTr("DClean")
    width: 640
    height: 480

    //menu containing two menu items
    menuBar: MenuBar {
        Menu {
            id: menu
            title: qsTr("File")
            MenuItem {
                text: qsTr("&Open")
                onTriggered: console.log("Open action triggered");
            }
            MenuItem {
                text: qsTr("Exit")
                onTriggered: Qt.quit();
            }
        }
    }

    header: ToolBar {
        RowLayout {
            anchors.fill: parent

            ToolButton {
                text: "<"
                enabled: stack.depth > 1
                onClicked: stack.pop()
            }

            Label {
                text: "Title"
                elide: Label.ElideRight
                Layout.fillWidth: true
            }
            /*
            ToolButton {
                text: ":"
                onClicked: menu.open()
            }*/
        }
    }

    StackView {
        id: stack
        anchors.fill: parent
        initialItem: "DataView.qml"
    }

    Component {
        id: homePage
        
        ListView {
            anchors.fill: parent
            model: contacts
            delegate: Component {
                Row {
                    spacing: 10
                    Text {text: name}
                    Text {text: age}
                }
            }
        }
    }

    ListModel {
        id: contacts

        ListElement {
            name: "Homes"
            age: 23
        }

        ListElement {
            name: "Samantha Smith"
            age: 24
        }
    }

    /*
    footer: Text {
        text: "Hello Footer"
    }*/
}