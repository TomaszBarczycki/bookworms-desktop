# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginpage.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget, QMessageBox)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(688, 446)
        Form.setStyleSheet(u" background-color: #fcf7ec ")
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"font-family: \"Nunito Sans\", sans-serif;\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 11)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setMaximumSize(QSize(280, 400))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"border-radius:7%;")
        self.label_4.setPixmap(QPixmap(u"Components/loginwithbooks.jpg"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(300, 400))
        self.frame.setStyleSheet(u"background-color: #dda57a ;\n"
"width: 270%;\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 20)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(65, 16777215))
        self.label_9.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(220, 16777215))
        self.lineEdit.setStyleSheet(u"border-bottom: 2px solid white;\n"
"color: white;\n"
"border-top: none;")
        self.lineEdit.setFrame(True)

        self.gridLayout_2.addWidget(self.lineEdit, 2, 0, 1, 1, Qt.AlignHCenter)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(105, 16777215))
        self.label_8.setStyleSheet(u"font-family: \"Nunito Sans\";")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1, Qt.AlignBottom)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(220, 16777215))
        self.lineEdit_2.setStyleSheet(u"border-bottom: 2px solid white;\n"
"color: white;\n"
"border-top: none;")
        self.lineEdit_2.setFrame(True)

        self.gridLayout_2.addWidget(self.lineEdit_2, 4, 0, 1, 1, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(150, 40))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border-radius:20px;\n"
"	height: 40%;\n"
"    font: 12pt \"Nunito Sans\";\n"
"    color: white;\n"
"    background-color: rgba(106, 38, 52, 0.9);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(106, 38, 52, 1);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(86, 18, 32, 1);\n"
"    border-style: inset;\n"
"};\n"
"")

        self.gridLayout_2.addWidget(self.pushButton, 6, 0, 1, 1, Qt.AlignHCenter)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(245, 16777215))
        self.label_3.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(300, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 8, 0, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 7, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame)


        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText("")
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>ssdfgsdfgsdfg</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; color:#ffffff;\">Has\u0142o:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Zaloguj si\u0119</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>ssdfgsdfgsdfg</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; color:#ffffff;\">Adres E-mail:</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Zaloguj", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\"><span style=\" font-size:9pt; color:#ffffff;\">Zapomnia\u0142e\u015b has\u0142a?</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ffffff;\">Nie masz konta? Zarejestruj si\u0119</span></p></body></html>", None))
    # retranslateUi

