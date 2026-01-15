# Prediksi Harga Motor Bekas Menggunakan Machine Learning

Nama        : Gia Khansa Khairunnisa  
NPM         : 2441062  
Program Studi : Sistem Informasi  
Mata Kuliah : Machine Learning  
Jenis Tugas : Ujian Akhir Semester (UAS)  

---

## Deskripsi Proyek
Proyek ini merupakan tugas Ujian Akhir Semester (UAS) pada mata kuliah Machine Learning.  
Proyek ini bertujuan untuk membangun sebuah sistem prediksi harga motor bekas menggunakan metode Machine Learning berbasis regresi.

Model Machine Learning dilatih menggunakan dataset motor bekas, kemudian disimpan dan diintegrasikan ke dalam aplikasi berbasis FastAPI. Aplikasi ini memungkinkan pengguna untuk melakukan prediksi harga motor bekas melalui antarmuka web sederhana.

---

## Tujuan Proyek
Tujuan dari pengembangan proyek ini adalah:
- Menerapkan konsep Machine Learning pada permasalahan nyata
- Melakukan pelatihan model regresi untuk memprediksi harga motor bekas
- Mengimplementasikan model Machine Learning ke dalam aplikasi berbasis web
- Memahami alur kerja Machine Learning mulai dari pengolahan data hingga deployment sederhana

---

## Dataset
Dataset yang digunakan dalam proyek ini adalah **BIKE DETAILS Dataset** yang diperoleh dari platform Kaggle.  
Dataset ini berisi data motor bekas yang dijual di India, dengan berbagai atribut yang berkaitan dengan spesifikasi dan harga motor.

Dataset disimpan dalam format CSV, yaitu:
- `BIKE DETAILS.csv`

Karena dataset berasal dari India, hasil prediksi harga motor ditampilkan dalam mata uang **Rupee (India)**.

---

## Algoritma yang Digunakan
Algoritma Machine Learning yang digunakan dalam proyek ini adalah **Regresi Linier (Linear Regression)**.

Regresi Linier dipilih karena:
- Cocok untuk memprediksi nilai numerik kontinu seperti harga
- Mudah diimplementasikan dan dipahami
- Memiliki interpretasi hasil yang sederhana
- Sesuai untuk tujuan pembelajaran pada mata kuliah Machine Learning

---

## Variabel Independen dan Dependen

### Variabel Independen (X)
Variabel input yang digunakan untuk memprediksi harga motor bekas, yaitu:
- `year` (tahun produksi motor)

### Variabel Dependen (Y)
Variabel target yang diprediksi oleh model, yaitu:
- `selling_price` (harga jual motor bekas)

---

## Metode dan Teknologi
Proyek ini menggunakan teknologi dan metode sebagai berikut:
- Metode Machine Learning : Regresi
- Bahasa Pemrograman : Python
- Framework API : FastAPI
- Library Pendukung:
  - pandas
  - numpy
  - scikit-learn
  - fastapi
  - uvicorn

---

## Struktur Folder Proyek
uas_ml_gia/
├── train.py # Script pelatihan model Machine Learning
├── main.py # Aplikasi FastAPI untuk prediksi harga motor
├── model_harga.pkl # File model hasil training
├── index.html # Antarmuka web
├── BIKE DETAILS.csv # Dataset motor bekas
├── requirements.txt # Daftar library
└── README.md # Dokumentasi proyek
---

1. Membuat Virtual Environment
```bash
python -m venv .venv
2. Mengaktifkan Virtual Environment
.venv\Scripts\activate
3. Menginstal Library
pip install -r requirements.txt
4. Melatih Model
python train.py
python train.py
5. Menjalankan Aplikasi FastAPI
python -m uvicorn main:app --reload
6. Membuka Aplikasi
Buka browser dan akses:
http://127.0.0.1:8000

---

Implementasi Sistem

Model Machine Learning yang telah dilatih disimpan dalam format .pkl dan digunakan kembali oleh aplikasi FastAPI.
Pengguna dapat memasukkan tahun produksi motor melalui antarmuka web untuk mendapatkan hasil prediksi harga motor bekas secara langsung.

Kesimpulan

Proyek ini berhasil menerapkan konsep Machine Learning dalam memprediksi harga motor bekas serta mengintegrasikannya ke dalam aplikasi berbasis web menggunakan FastAPI.
Melalui proyek ini, mahasiswa dapat memahami alur lengkap pengembangan sistem Machine Learning mulai dari pengolahan data, pelatihan model, hingga deployment sederhana.
