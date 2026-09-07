# Data Mining Week 3 - Data Preprocessing dan Normalisasi

Repository ini berisi materi dan praktik lanjutan preprocessing data dengan fokus pada handling missing values, normalisasi, dan standardisasi data menggunakan dataset Titanic dan Ruspini.

## 📋 Deskripsi

Proyek ini merupakan bagian dari pembelajaran Data Mining Week 3 yang fokus pada teknik preprocessing lanjutan, termasuk imputasi missing values, min-max normalization, z-score standardization, dan sigmoid normalization.

## 📁 Struktur Proyek

```
week 3/
├── 1.py                    # Membaca dan menampilkan dataset
├── 2.py                    # Menghitung dimensi dataset
├── 3.py                    # Seleksi fitur Age dan Fare
├── 4.py                    # Ekstraksi target variable (Survived)
├── 5.py                    # Imputasi missing values dengan mean per group
├── 6.py                    # Min-Max Normalization (0-1 scaling)
├── 7.py                    # Z-Score Standardization
├── 8.py                    # Sigmoid Normalization
├── latihan.py              # Latihan missing values dengan Ruspini dataset
├── titanic.csv             # Dataset Titanic
├── ruspini_missing.csv     # Dataset Ruspini dengan missing values
└── README.md
```

## 🎯 Tujuan Pembelajaran

- Menangani missing values dengan teknik imputasi
- Memahami dan mengimplementasikan teknik normalisasi data
- Melakukan standardisasi data menggunakan Z-Score
- Mengaplikasikan transformasi sigmoid
- Preprocessing data untuk machine learning

## 🔧 Prerequisites

Pastikan Anda telah menginstall:
- Python 3.x
- pandas
- numpy

## 📦 Instalasi

1. Clone repository ini:
```bash
git clone https://github.com/KH-kemal/DM_M2.git
cd DM_M2/week\ 3
```

2. Install dependencies:
```bash
pip install pandas numpy
```

## 🚀 Cara Penggunaan

Setiap file Python dapat dijalankan secara independen:

```bash
python 1.py
```

### Deskripsi File

**1.py** - Membaca Dataset
- Membaca file CSV Titanic
- Menampilkan seluruh dataset

**2.py** - Dimensi Dataset
- Menghitung jumlah baris dan kolom
- Menampilkan shape dataset

**3.py** - Seleksi Fitur
- Memilih kolom Age dan Fare
- Menampilkan data fitur numerik

**4.py** - Ekstraksi Target
- Mengekstrak kolom Survived (target variable)
- Menampilkan data kelas

**5.py** - Imputasi Missing Values
- Menghitung jumlah missing values sebelum imputasi
- Mengisi missing values Age dengan mean berdasarkan Pclass
- Menampilkan hasil setelah imputasi

**6.py** - Min-Max Normalization
- Imputasi missing values terlebih dahulu
- Normalisasi Age dan Fare ke range [0, 1]
- Formula: (x - min) / (max - min)
- Menampilkan data original dan normalized

**7.py** - Z-Score Standardization
- Imputasi missing values terlebih dahulu
- Standardisasi Age dan Fare menggunakan Z-Score
- Formula: (x - mean) / std
- Menampilkan data dengan z-score

**8.py** - Sigmoid Normalization
- Imputasi missing values terlebih dahulu
- Standardisasi dengan Z-Score manual (ddof=0)
- Transformasi sigmoid: 1 / (1 + e^(-z))
- Menampilkan data original, z-score, dan sigmoid

**latihan.py** - Praktik Ruspini Dataset
- Membaca dataset Ruspini dengan missing values
- Mengisi missing values dengan mean per class
- Menampilkan dataset sebelum dan sesudah imputasi

## 📊 Dataset

### Titanic Dataset
Dataset yang berisi informasi penumpang kapal Titanic dengan fitur:
- **Age**: Usia penumpang (memiliki missing values)
- **Fare**: Harga tiket
- **Pclass**: Kelas tiket (digunakan untuk grouping imputasi)
- **Survived**: Target variable (0 = Tidak selamat, 1 = Selamat)

### Ruspini Dataset
Dataset clustering dengan missing values yang digunakan untuk latihan imputasi berdasarkan class grouping.

## 📈 Teknik Preprocessing yang Diimplementasikan

### 1. Missing Values Handling
- **Group-based Mean Imputation**: Mengisi missing values dengan rata-rata berdasarkan grup (Pclass)
- Diimplementasikan di: `5.py`, `6.py`, `7.py`, `8.py`

### 2. Min-Max Normalization
- Menskalakan data ke range [0, 1]
- Formula: `(x - min) / (max - min)`
- Diimplementasikan di: `6.py`

### 3. Z-Score Standardization
- Menskalakan data dengan mean = 0 dan std = 1
- Formula: `(x - mean) / std`
- Diimplementasikan di: `7.py`, `8.py`

### 4. Sigmoid Normalization
- Transformasi non-linear menggunakan fungsi sigmoid
- Formula: `1 / (1 + e^(-z))`
- Menghasilkan nilai dalam range [0, 1]
- Diimplementasikan di: `8.py`

## 💡 Catatan Penting

- Imputasi missing values dilakukan sebelum normalisasi/standardisasi
- Group-based imputation (berdasarkan Pclass) lebih baik daripada global mean
- Pilih teknik normalisasi sesuai kebutuhan algoritma ML:
  - Min-Max: untuk algoritma yang sensitif terhadap skala (Neural Networks, KNN)
  - Z-Score: untuk algoritma yang mengasumsikan distribusi normal
  - Sigmoid: untuk transformasi non-linear dan bounded output

## 👨‍💻 Author

**KH-kemal**
- GitHub: [@KH-kemal](https://github.com/KH-kemal)

## 📝 Catatan

Proyek ini dibuat untuk keperluan pembelajaran Data Mining. Dataset dan kode dapat dimodifikasi sesuai kebutuhan pembelajaran.

## 📄 License

Proyek ini dibuat untuk keperluan edukasi.

---
*Last updated: September 2026*
