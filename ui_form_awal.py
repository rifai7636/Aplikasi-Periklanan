# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(800, 600)
        self.actionData_Client = QAction(Main)
        self.actionData_Client.setObjectName(u"actionData_Client")
        self.actionData_Iklan = QAction(Main)
        self.actionData_Iklan.setObjectName(u"actionData_Iklan")
        self.actionInvoice = QAction(Main)
        self.actionInvoice.setObjectName(u"actionInvoice")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 18))
        self.menuMain = QMenu(self.menubar)
        self.menuMain.setObjectName(u"menuMain")
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMain.menuAction())
        self.menuMain.addAction(self.actionData_Client)
        self.menuMain.addAction(self.actionData_Iklan)
        self.menuMain.addAction(self.actionInvoice)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Main", None))
        self.actionData_Client.setText(QCoreApplication.translate("Main", u"Data Client", None))
        self.actionData_Iklan.setText(QCoreApplication.translate("Main", u"Data Iklan", None))
        self.actionInvoice.setText(QCoreApplication.translate("Main", u"Invoice", None))
        self.menuMain.setTitle(QCoreApplication.translate("Main", u"Main", None))
    # retranslateUi

