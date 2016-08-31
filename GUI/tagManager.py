# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tagManager.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TagManager(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(316, 295)
        self.tagsList = QtWidgets.QListWidget(Dialog)
        self.tagsList.setGeometry(QtCore.QRect(0, 0, 171, 291))
        self.tagsList.setObjectName("tagsList")
        self.modifyButton = QtWidgets.QPushButton(Dialog)
        self.modifyButton.setGeometry(QtCore.QRect(200, 80, 81, 23))
        self.modifyButton.setObjectName("modifyButton")
        self.OKButton = QtWidgets.QPushButton(Dialog)
        self.OKButton.setGeometry(QtCore.QRect(190, 260, 111, 23))
        self.OKButton.setObjectName("OKButton")
        self.deleteButton = QtWidgets.QPushButton(Dialog)
        self.deleteButton.setGeometry(QtCore.QRect(200, 120, 81, 23))
        self.deleteButton.setObjectName("deleteButton")
        self.addNewTagButton = QtWidgets.QPushButton(Dialog)
        self.addNewTagButton.setGeometry(QtCore.QRect(200, 40, 81, 23))
        self.addNewTagButton.setObjectName("addNewTagButton")
        self.searchTagsLineEdit = QtWidgets.QLineEdit(Dialog)
        self.searchTagsLineEdit.setGeometry(QtCore.QRect(180, 10, 113, 20))
        self.searchTagsLineEdit.setObjectName("searchTagsLineEdit")
        self.choseTagsTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.choseTagsTextEdit.setGeometry(QtCore.QRect(190, 170, 111, 71))
        self.choseTagsTextEdit.setObjectName("choseTagsTextEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tag Manager"))
        self.modifyButton.setText(_translate("Dialog", "Modify"))
        self.OKButton.setText(_translate("Dialog", "Add"))
        self.deleteButton.setText(_translate("Dialog", "Delete"))
        self.addNewTagButton.setText(_translate("Dialog", "Add a New Tag"))
        self.searchTagsLineEdit.setPlaceholderText(_translate("Dialog", "Search Tags"))
        self.choseTagsTextEdit.setPlaceholderText(_translate("Dialog", "Chosen Tags"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_TagManager()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

