# Data Mining Week 2 - Preprocessing

Repository ini berisi materi dan praktik preprocessing data menggunakan dataset Titanic untuk pembelajaran Data Mining.

## 📋 Deskripsi

Proyek ini merupakan bagian dari pembelajaran Data Mining Week 2 yang fokus pada teknik preprocessing data. Menggunakan dataset Titanic, proyek ini mencakup berbagai operasi dasar analisis data dan visualisasi menggunakan Python dan Pandas.

## 📁 Struktur Proyek

```
week 2/
├── preprossecing/
│   ├── 1.py              # Membaca dan menampilkan dataset
│   ├── 2.py              # Menghitung jumlah baris dan kolom
│   ├── 3.py              # Seleksi kolom spesifik
│   ├── 4.py              # Ekstraksi kolom target (Survived)
│   ├── 5.py              # Membuat fitur baru (Relatives)
│   ├── 6.py              # Analisis distribusi Pclass
│   ├── 7.py              # Analisis distribusi Sex
│   ├── 8.py              # Crosstab Pclass vs Survived
│   ├── 9.py              # Visualisasi Sex vs Survived
│   └── titanic.csv       # Dataset Titanic
└── README.md
```

## 🎯 Tujuan Pembelajaran

- Memahami dasar-dasar preprocessing data
- Eksplorasi dan analisis dataset
- Seleksi dan transformasi fitur
- Visualisasi data untuk insight
- Penggunaan Pandas untuk manipulasi data

## 🔧 Prerequisites

Pastikan Anda telah menginstall:
- Python 3.x
- pandas
- matplotlib

## 📦 Instalasi

1. Clone repository ini:
```bash
git clone https://github.com/KH-kemal/DM_M2.git
cd DM_M2
```

2. Install dependencies:
```bash
pip install pandas matplotlib
```

## 🚀 Cara Penggunaan

Setiap file Python dapat dijalankan secara independen:

```bash
cd preprossecing
python 1.py
```

### Deskripsi File

**1.py** - Membaca Dataset
- Membaca file CSV Titanic
- Menampilkan seluruh dataset

**2.py** - Dimensi Dataset
- Menghitung jumlah baris dan kolom
- Menampilkan shape dataset

**3.py** - Seleksi Kolom
- Memilih kolom: Name, Sex, Age, Pclass, Fare
- Menampilkan data terpilih

**4.py** - Ekstraksi Target
- Mengekstrak kolom Survived (target variable)
- Menampilkan hasil

**5.py** - Feature Engineering
- Membuat fitur baru "Relatives"
- Menggabungkan SibSp dan Parch
- Menampilkan data dengan fitur baru

**6.py** - Analisis Pclass
- Menghitung distribusi kelas penumpang
- Menampilkan value counts

**7.py** - Analisis Gender
- Menghitung distribusi jenis kelamin
- Menampilkan value counts

**8.py** - Crosstab Analysis
- Membuat tabel silang Pclass vs Survived
- Analisis survival rate per kelas

**9.py** - Visualisasi
- Membuat scatter plot Sex vs Survived
- Menyimpan visualisasi ke file PNG

## 📊 Dataset

Dataset yang digunakan adalah **Titanic Dataset** yang berisi informasi penumpang kapal Titanic dengan fitur:
- **PassengerId**: ID unik penumpang
- **Survived**: Status keselamatan (0 = Tidak selamat, 1 = Selamat)
- **Pclass**: Kelas tiket (1, 2, 3)
- **Name**: Nama penumpang
- **Sex**: Jenis kelamin
- **Age**: Usia
- **SibSp**: Jumlah saudara/pasangan di kapal
- **Parch**: Jumlah orang tua/anak di kapal
- **Fare**: Harga tiket
- **Embarked**: Pelabuhan keberangkatan

## 📈 Output

Script visualisasi (9.py) akan menghasilkan:
- `plot_9.png`: Scatter plot visualisasi Sex vs Survived

## 👨‍💻 Author

**KH-kemal**
- GitHub: [@KH-kemal](https://github.com/KH-kemal)

## 📝 Catatan

Proyek ini dibuat untuk keperluan pembelajaran Data Mining. Dataset dan kode dapat dimodifikasi sesuai kebutuhan pembelajaran.

## 📄 License

Proyek ini dibuat untuk keperluan edukasi.

---
*Last updated: September 2026*
