import sys
from PyQt5 import QtWidgets
from .tagManager import Ui_TagManager


class tagManagerController(Ui_TagManager):
    def __init__(self, dialog):
        Ui_TagManager.__init__(self)
        self.setupUi(dialog)

        # Connect buttons with custom functions
        self.addNewTagButton.clicked.connect(self.addNewTag)
        self.modifyButton.clicked.connect(self.modifyTag)
        self.deleteButton.clicked.connect(self.deleteTag)
        self.OKButton.clicked.connect(self.done)
        self.thread.connect(self.thread, SIGNAL("selectedItemsToString()"), self.choseTagsTextEdit.setPlainText)

    def selectedItemsToString(self):
        list = self.tagsList.selectedItems()
        return " ".join(list)  # is this the same ? if yes hit yourself!
        # Abtin and Zahra Code!
        # result = ""
        # for item in list:
        #     result += item + " "
        # return result

    def addNewTag(self):
        return

    def modifyTag(self):
        return

    def deleteTag(self):
        return

    def done(self):
        self.tagsList.addItem("item1")
        self.tagsList.addItem("item2")
        self.tagsList.addItem("item3")
        self.tagsList.addItem("item4")
        return

    def handleTagList(self):  # pay attention to show tags in chosen tags
        # pay attention to filter tags according to text written in the filter part
        return


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    prog = tagManagerController(dialog)
    dialog.show()
    sys.exit(app.exec_())
