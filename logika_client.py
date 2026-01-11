from PySide6.QtWidgets import QMessageBox
from database import Database


class LogikaClient:
    def __init__(self, ui):
        self.ui = ui
        self.db = Database()

        # HUBUNGKAN BUTTON
        self.ui.btnTambah.clicked.connect(self.tambah)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBersih.clicked.connect(self.bersih)

    def tambah(self):
        nama = self.ui.txtNama.text()
        alamat = self.ui.txtAlamat.text()
        telp = self.ui.txtTelepon.text()

        if not nama or not telp:
            QMessageBox.warning(None, "Validasi", "Nama dan Telepon wajib diisi")
            return

        self.db.insert_client(nama, alamat, telp)
        QMessageBox.information(None, "Sukses", "Data client berhasil disimpan")
        self.bersih()

    def ubah(self):
        id_client = self.ui.txtId.text()
        nama = self.ui.txtNama.text()
        alamat = self.ui.txtAlamat.text()
        telp = self.ui.txtTelepon.text()

        if not id_client:
            QMessageBox.warning(None, "Validasi", "ID belum diisi")
            return

        self.db.update_client(id_client, nama, alamat, telp)
        QMessageBox.information(None, "Sukses", "Data client berhasil diubah")

    def hapus(self):
        id_client = self.ui.txtId.text()

        if not id_client:
            QMessageBox.warning(None, "Validasi", "ID belum diisi")
            return

        self.db.delete_client(id_client)
        QMessageBox.information(None, "Sukses", "Data client berhasil dihapus")
        self.bersih()

    def bersih(self):
        self.ui.txtId.clear()
        self.ui.txtNama.clear()
        self.ui.txtAlamat.clear()
        self.ui.txtTelepon.clear()
