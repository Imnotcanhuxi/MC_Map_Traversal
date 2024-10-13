# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(557, 397)
        Form.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        icon.addFile(u"favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(9, 9, 211, 381))
        self.groupBox.setCursor(QCursor(Qt.ArrowCursor))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 5, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 6, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 8, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 9, 0, 1, 1)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)

        self.gridLayout.addWidget(self.pushButton, 10, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(227, 9, 321, 276))
        self.plainTextEdit_2 = QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(10, 20, 301, 241))
        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(227, 291, 321, 97))
        self.plainTextEdit = QPlainTextEdit(self.groupBox_3)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 20, 301, 71))
        self.plainTextEdit.setUndoRedoEnabled(False)
        self.plainTextEdit.setReadOnly(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"MCIBEMOD\u5730\u56fe\u904d\u5386\u8f85\u52a9\u5de5\u5177", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u904d\u5386\u6570\u91cf\u8f93\u5165\u6846(\u53ea\u7528\u586b\u4f60\u9700\u8981\u7684\u4e00\u884c)", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u6700\u5f00\u59cb\u7684\u5730\u56fe\u753b\u7f16\u53f7", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5730\u56fe\u753b\u7f16\u53f7(\u5fc5\u586b)", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u904d\u5386\u6570\u91cf", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u4f60\u8981\u904d\u5386\u7684\u6570\u91cf(<=729)", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5730\u56fe\u753b\u7684\u957f\u548c\u5bbd", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5730\u56fe\u753b\u7684\u5bbd", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5730\u56fe\u753b\u7684\u957f", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u4e24\u4e2a\u4e0d\u540c\u5730\u56fe\u753b\u7f16\u53f7\u7684\u5dee", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u7b2c\u4e00\u4e2a\u5730\u56fe\u753b\u7684\u7f16\u53f7", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u7b2c\u4e8c\u4e2a\u5730\u56fe\u753b\u7684\u7f16\u53f7", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u751f\u6210!", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u8f93\u51fa", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u547d\u4ee4\u8f93\u51fa(\u8f85\u52a9)", None))
    # retranslateUi

