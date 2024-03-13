# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startpage.ui'
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
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(667, 726)
        Form.setStyleSheet(u" background-color: #fcf7ec ")
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"logo{\n"
"height:50%;\n"
"width: auto;\n"
"};\n"
"background-color: #fcf7ec; ")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u" font-size: 45px;\n"
" font-family: \"Nunito Sans\";")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMaximumSize(QSize(500, 800))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(700, 16777215))

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QPushButton {\n"
"    height: 40%;\n"
"    width: 20%;\n"
"    font: 12pt \"Nunito Sans\";\n"
"    color: white;\n"
"    background-color: rgba(106, 38, 52, 0.9);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(106, 38, 52, 1);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(86, 18, 32, 1);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 50, -1, -1)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(300, 40))
        self.pushButton.setStyleSheet(u"border-radius: 10px;\n"
"width: 250%")

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(300, 40))
        self.pushButton_2.setStyleSheet(u"border-radius:10px;\n"
"width: 250%;")

        self.verticalLayout.addWidget(self.pushButton_2, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame)


        self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 2, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(200, 150))
        self.label.setPixmap(QPixmap(u"Components/bookwormsLogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 2, 4, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:27pt; font-weight:600;\">Bookworms</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt;\">Je\u017celi szukasz miejsca, w kt\u00f3rym mo\u017cesz porz\u0105dkowa\u0107</span></p><p><span style=\" font-size:10pt;\">swoj\u0105 biblioteczk\u0119, to Bookworms jest dla Ciebie!</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt;\">Mo\u017cesz dodawa\u0107 ksi\u0105\u017cki jako: przeczytane, do</span></p><p><span style=\" font-size:10pt;\">przeczytania oraz aktualnie czytane. Wszystko w</span></p><p><span style=\" font-size:10pt;\">jednym miejscu!</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt;\">Nie masz jeszcze konta? Zach\u0119camy do rejestracji!</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600;\">Zesp\u00f3\u0142 Bookworms</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Zaloguj", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Zarejestruj", None))
        self.label.setText("")
    # retranslateUi

