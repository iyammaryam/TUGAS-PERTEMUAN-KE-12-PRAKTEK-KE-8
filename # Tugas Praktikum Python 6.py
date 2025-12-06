# Tugas Praktikum Python

## 1. Program Daftar Nilai Mahasiswa

Berisi fungsi: tambah(), tampilkan(), hapus(nama), ubah(nama).

### **Kode Program (Python)**

python
data_mahasiswa = {}

def tambah():
    nama = input("Masukkan nama mahasiswa: ")
    nilai = float(input("Masukkan nilai: "))
    data_mahasiswa[nama] = nilai
    print("Data berhasil ditambahkan!\n")

def tampilkan():
    if not data_mahasiswa:
        print("Belum ada data.\n")
    else:
        print("Daftar Nilai Mahasiswa:")
        for nama, nilai in data_mahasiswa.items():
            print(f"{nama}: {nilai}")
        print()

def hapus(nama):
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"Data {nama} berhasil dihapus!\n")
    else:
        print("Nama tidak ditemukan.\n")

def ubah(nama):
    if nama in data_mahasiswa:
        nilai_baru = float(input("Masukkan nilai baru: "))
        data_mahasiswa[nama] = nilai_baru
        print("Data berhasil diubah!\n")
    else:
        print("Nama tidak ditemukan.\n")

# Menu utama
while True:
    print("=== MENU UTAMA ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah()
    elif pilih == "2":
        tampilkan()
    elif pilih == "3":
        nama = input("Masukkan nama yang akan dihapus: ")
        hapus(nama)
    elif pilih == "4":
        nama = input("Masukkan nama yang akan diubah: ")
        ubah(nama)
    elif pilih == "5":
        print("Keluar...")
        break
    else:
        print("Pilihan tidak valid!\n")
```

---

## **2. Flowchart Program

(Dalam bentuk teks ASCII)**

```
           +-------------------+
           |   Mulai Program   |
           +---------+---------+
                     |
                     v
            +-----------------+
            | Tampilkan Menu  |
            +-----------------+
                     |
                     v
           +-------------------+
           |   Input Pilihan   |
           +---------+---------+
                     |
    ------------------------------------------------------
    |            |             |             |           |
    v            v             v             v           v
+-------+   +----------+   +-----------+  +----------+ +---------+
|Tambah|   |Tampilkan |   |   Hapus   |  |   Ubah   | |  Keluar |
+---+---+   +----+-----+   +-----+-----+  +-----+----+ +----+----+
    |            |             |             |            |
    v            v             v             v            v
Tambah data?  Cetak data    Input nama    Input nama     Selesai
    |            |      apakah ada?      apakah ada?
    |            |             |             |
    +------------+-------------+-------------+
                     kembali ke menu
```

---

## **3. Penjelasan Alur Program**

### 1. **Mulai Program**

Program dimulai dan memasuki loop menu utama.

### 2. **Menampilkan Menu**

Program menampilkan opsi: tambah, tampilkan, hapus, ubah, keluar.

### 3. **Input Pilihan**

Pengguna memilih aksi yang ingin dijalankan.

### 4. **Fungsi tambah()**

* Pengguna memasukkan nama dan nilai.
* Data disimpan ke dictionary `data_mahasiswa`.

### 5. **Fungsi tampilkan()**

* Jika kosong → tampilkan pesan.
* Jika ada → daftar nama dan nilai ditampilkan.

### 6. **Fungsi hapus(nama)**

* Cek apakah nama ada.
* Jika ada → hapus dari dictionary.
* Jika tidak → tampilkan pesan error.

### 7. **Fungsi ubah(nama)**

* Cek apakah nama ada.
* Jika ada → minta nilai baru dan update.

### 8. **Keluar Program**

* Program berhenti setelah memilih opsi "Keluar".

---

## 4. Latihan 1 (Mengubah Fungsi ke Lambda)

python
import math

a = lambda x: x**2
b = lambda x, y: math.sqrt(x**2 + y**2)
c = lambda *args: sum(args)/len(args)
d = lambda s: "".join(set(s))