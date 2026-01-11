# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(460, 356)
        self.vboxLayout = QVBoxLayout(Form)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.label)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(6)
        self.label1 = QLabel(Form)
        self.label1.setObjectName(u"label1")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label1)

        self.txtIdClient = QLineEdit(Form)
        self.txtIdClient.setObjectName(u"txtIdClient")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtIdClient)

        self.label2 = QLabel(Form)
        self.label2.setObjectName(u"label2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label2)

        self.txtIdAdmin = QLineEdit(Form)
        self.txtIdAdmin.setObjectName(u"txtIdAdmin")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtIdAdmin)

        self.label3 = QLabel(Form)
        self.label3.setObjectName(u"label3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label3)

        self.txtNama = QLineEdit(Form)
        self.txtNama.setObjectName(u"txtNama")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtNama)

        self.label4 = QLabel(Form)
        self.label4.setObjectName(u"label4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label4)

        self.txtPerusahaan = QLineEdit(Form)
        self.txtPerusahaan.setObjectName(u"txtPerusahaan")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtPerusahaan)

        self.label5 = QLabel(Form)
        self.label5.setObjectName(u"label5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label5)

        self.txtAlamat = QTextEdit(Form)
        self.txtAlamat.setObjectName(u"txtAlamat")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtAlamat)

        self.label6 = QLabel(Form)
        self.label6.setObjectName(u"label6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label6)

        self.txtTelp = QLineEdit(Form)
        self.txtTelp.setObjectName(u"txtTelp")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.txtTelp)


        self.hboxLayout.addLayout(self.formLayout)

        self.vboxLayout1 = QVBoxLayout()
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.btnTambah = QPushButton(Form)
        self.btnTambah.setObjectName(u"btnTambah")

        self.vboxLayout1.addWidget(self.btnTambah)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.vboxLayout1.addWidget(self.btnSimpan)

        self.btnEdit = QPushButton(Form)
        self.btnEdit.setObjectName(u"btnEdit")

        self.vboxLayout1.addWidget(self.btnEdit)

        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")

        self.vboxLayout1.addWidget(self.btnHapus)

        self.btnTutup = QPushButton(Form)
        self.btnTutup.setObjectName(u"btnTutup")

        self.vboxLayout1.addWidget(self.btnTutup)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout1.addItem(self.verticalSpacer)


        self.hboxLayout.addLayout(self.vboxLayout1)


        self.vboxLayout.addLayout(self.hboxLayout)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.label7 = QLabel(Form)
        self.label7.setObjectName(u"label7")

        self.hboxLayout1.addWidget(self.label7)

        self.txtCari = QLineEdit(Form)
        self.txtCari.setObjectName(u"txtCari")

        self.hboxLayout1.addWidget(self.txtCari)

        self.btnCari = QPushButton(Form)
        self.btnCari.setObjectName(u"btnCari")

        self.hboxLayout1.addWidget(self.btnCari)


        self.vboxLayout.addLayout(self.hboxLayout1)

        self.tableClient = QTableWidget(Form)
        if (self.tableClient.columnCount() < 6):
            self.tableClient.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableClient.setObjectName(u"tableClient")
        self.tableClient.setColumnCount(6)

        self.vboxLayout.addWidget(self.tableClient)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Entry Data Client", None))
        self.label.setStyleSheet(QCoreApplication.translate("Form", u"font-size:16px;font-weight:bold;", None))
        self.label.setText(QCoreApplication.translate("Form", u"ENTRY DATA CLIENT", None))
        self.label1.setText(QCoreApplication.translate("Form", u"ID Client", None))
        self.label2.setText(QCoreApplication.translate("Form", u"ID Admin", None))
        self.label3.setText(QCoreApplication.translate("Form", u"Nama Lengkap", None))
        self.label4.setText(QCoreApplication.translate("Form", u"Perusahaan", None))
        self.label5.setText(QCoreApplication.translate("Form", u"Alamat", None))
        self.label6.setText(QCoreApplication.translate("Form", u"No. Telp", None))
        self.btnTambah.setText(QCoreApplication.translate("Form", u"\u2795 Tambah", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"\U0001f4be Simpan", None))
        self.btnEdit.setText(QCoreApplication.translate("Form", u"\u270f\ufe0f Edit", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"\U0001f5d1 Hapus", None))
        self.btnTutup.setText(QCoreApplication.translate("Form", u"\u274c Tutup", None))
        self.label7.setText(QCoreApplication.translate("Form", u"Cari", None))
        self.btnCari.setText(QCoreApplication.translate("Form", u"\U0001f50d", None))
        ___qtablewidgetitem = self.tableClient.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Client", None));
        ___qtablewidgetitem1 = self.tableClient.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"ID Admin", None));
        ___qtablewidgetitem2 = self.tableClient.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Nama", None));
        ___qtablewidgetitem3 = self.tableClient.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Perusahaan", None));
        ___qtablewidgetitem4 = self.tableClient.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Alamat", None));
        ___qtablewidgetitem5 = self.tableClient.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"No. Telp", None));
    # retranslateUi

