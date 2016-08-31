import sys
from PyQt5 import QtWidgets
from new import Ui_NEW
from tagManager import Ui_TagManager


class MyFirstGuiProgram(Ui_NEW):
    def __init__(self, dialog):
        Ui_NEW.__init__(self)
        self.setupUi(dialog)

        # Connect "add" button with a custom function (ok)
        self.OKButton.clicked.connect(self.ok)
        self.toolButton.clicked.connect(self.showDial)


    def ok(self):
        print("ok clicked")

    def showDial(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_TagManager()
        ui.setupUi(Dialog)
        Dialog.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    prog = MyFirstGuiProgram(dialog)
    dialog.show()
    sys.exit(app.exec_())
