from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor, QPixmap
from Ui_main_2 import Ui_Form
import pyperclip


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()

    def bind(self):
        self.lineEdit.setDisabled(True)
        self.lineEdit_2.setDisabled(True)
        self.lineEdit_3.setDisabled(True)
        self.lineEdit_4.setDisabled(True)
        self.lineEdit_5.setDisabled(True)
        self.pushButton.setDisabled(True)
        self.radioButton.toggled.connect(self.check)
        self.radioButton_2.toggled.connect(self.check_2)
        self.radioButton_3.toggled.connect(self.check_3)
        self.pushButton.clicked.connect(self.main)

    def main(self):
        if self.radioButton.isChecked():
            if self.lineEdit.text() == "":
                self.plainTextEdit.appendPlainText("请输入地图画遍历的数量!")
        elif self.radioButton_2.isChecked():
            if self.lineEdit_2.text() == "" and self.lineEdit_3.text() == "":
                self.plainTextEdit.appendPlainText("请输入地图画的长宽!")
            elif self.lineEdit_2.text() == "":
                self.plainTextEdit.appendPlainText("请输入地图画的宽度!")
            elif self.lineEdit_3.text() == "":
                self.plainTextEdit.appendPlainText("请输入地图画的高度!")
        elif self.radioButton_3.isChecked():
            if self.lineEdit_4.text() == "" and self.lineEdit_5.text() == "":
                self.plainTextEdit.appendPlainText("请输入两幅地图画的编号!")
            elif self.lineEdit_4.text() == "":
                self.plainTextEdit.appendPlainText("请输入第一幅地图画的编号!")
            elif self.lineEdit_5.text() == "":
                self.plainTextEdit.appendPlainText("请输入第二幅地图画的编号!")

    def check(self):
        if self.radioButton.isChecked():
            self.lineEdit.setDisabled(False)
            self.pushButton.setDisabled(False)
        else:
            self.lineEdit.setDisabled(True)

    def check_2(self):
        if self.radioButton_2.isChecked():
            self.lineEdit_2.setDisabled(False)
            self.lineEdit_3.setDisabled(False)
            self.pushButton.setDisabled(False)
        else:
            self.lineEdit_2.setDisabled(True)
            self.lineEdit_3.setDisabled(True)

    def check_3(self):
        if self.radioButton_3.isChecked():
            self.lineEdit_4.setDisabled(False)
            self.lineEdit_5.setDisabled(False)
            self.pushButton.setDisabled(False)
        else:
            self.lineEdit_4.setDisabled(True)
            self.lineEdit_5.setDisabled(True)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
