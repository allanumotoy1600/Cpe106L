import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from singup import signUp_Dialog
from login import Ui_Dialog


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
