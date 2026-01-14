Project UAS Mata Kuliah Machine Learning  
Nama: Gia Khansa  
Studi Kasus: Prediksi Harga Motor Bekas  

## Deskripsi
Project ini mengimplementasikan alur kerja Machine Learning secara end-to-end, mulai dari preprocessing data, pelatihan model, hingga deployment model menggunakan FastAPI dan antarmuka web sederhana.

Dataset yang digunakan adalah BIKE DETAILS dari Kaggle yang berasal dari India, sehingga harga motor dinyatakan dalam mata uang Rupee (₹).

## Dataset
- Sumber: Kaggle – BIKE DETAILS
- Variabel independen (X): year
- Variabel dependen (y): selling_price

## Algoritma
Model yang digunakan adalah Linear Regression.

## Cara Menjalankan
```bash
pip install -r requirements.txt
python train.py
python -m uvicorn main:app --reload
