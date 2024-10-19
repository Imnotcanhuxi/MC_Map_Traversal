# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(447, 338)
        icon = QIcon()
        icon.addFile(u"favicon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 171, 91))
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QRect(10, 20, 95, 19))
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(False)
        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(10, 40, 95, 19))
        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(10, 60, 161, 19))
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 110, 171, 221))
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 61, 16))
        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 40, 151, 21))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 61, 16))
        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 90, 71, 21))
        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(90, 90, 71, 21))
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 120, 141, 16))
        self.lineEdit_4 = QLineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(10, 140, 151, 21))
        self.lineEdit_5 = QLineEdit(self.groupBox_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(10, 160, 151, 21))
        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 190, 151, 23))
        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(190, 70, 251, 261))
        self.plainTextEdit = QPlainTextEdit(self.groupBox_3)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 20, 231, 231))
        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(189, 10, 251, 51))
        self.inputEdit = QLineEdit(self.groupBox_4)
        self.inputEdit.setObjectName(u"inputEdit")
        self.inputEdit.setGeometry(QRect(10, 20, 231, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"MCIBEMOD\u5730\u56fe\u904d\u5386\u8f85\u52a9\u5de5\u5177 V2", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u9009\u62e9", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u6309\u6570\u91cf\u904d\u5386", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u6309\u957f\u5bbd\u904d\u5386", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"\u4e24\u4e2a\u4e0d\u540c\u5730\u56fe\u753b\u7684\u5dee\u904d\u5386", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u64cd\u4f5c(\u6570\u91cf<729)", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6309\u6570\u91cf\u904d\u5386", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6309\u957f\u5bbd\u904d\u5386", None))
#if QT_CONFIG(accessibility)
        self.lineEdit_2.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u957f", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"\u5bbd", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u4e24\u4e2a\u4e0d\u540c\u5730\u56fe\u753b\u7684\u5dee\u904d\u5386", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"\u7b2c\u4e00\u4e2a", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Form", u"\u7b2c\u4e8c\u4e2a", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u751f\u6210!", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u8f93\u51fa", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"\u8f93\u5165", None))
        self.inputEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5730\u56fe\u753b\u7b2c\u4e00\u4e2a\u904d\u5386\u7684\u7f16\u53f7", None))
    # retranslateUi

