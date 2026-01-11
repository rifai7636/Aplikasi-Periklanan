# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_form_awal import Ui_MainWindow
from client_window import ClientWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # MENU → DATA CLIENT
        self.ui.actionData_Client.triggered.connect(self.buka_client)

    def buka_client(self):
        self.client = ClientWindow()
        self.client.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
