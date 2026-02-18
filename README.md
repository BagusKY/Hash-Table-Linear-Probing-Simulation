# 📚 Struktur Data — Hash-Based Practice Problems

Repository ini berisi kumpulan latihan Struktur Data yang berfokus pada penggunaan **Hash Table**, baik melalui `set` maupun `dictionary (dict)` di Python.

Seluruh soal dirancang untuk memahami bagaimana hashing membantu meningkatkan efisiensi pencarian dan pengolahan data menjadi rata-rata **O(1)**.

---

# 🧠 Konsep Utama

Semua latihan dalam repository ini berbasis pada konsep:

* Hash Table
* Set
* Dictionary
* Collision handling (konsep dasar)
* Kompleksitas waktu (Big-O)

Python `set` dan `dict` secara internal menggunakan **hash table**, sehingga operasi seperti:

* Pencarian
* Penambahan
* Penghapusan

dapat dilakukan dalam waktu rata-rata **O(1)**.

---

# 📂 Daftar Soal

---

## 1️⃣ Deduplication

### 🎯 Tujuan

Menghapus elemen duplikat dari sebuah list tanpa mengubah urutan kemunculan pertama.

### 💡 Konsep

Menggunakan `set` untuk melacak elemen yang sudah pernah muncul.

### 🧾 Contoh

Input:

```
[1, 2, 2, 3, 4, 3, 5]
```

Output:

```
[1, 2, 3, 4, 5]
```

### ⏱ Kompleksitas

* Waktu: O(n)
* Ruang: O(n)

---

## 2️⃣ Intersection Dua Array

### 🎯 Tujuan

Mengembalikan elemen yang muncul di kedua array.

### 💡 Konsep

Mengubah salah satu array menjadi `set` agar pencarian lebih cepat.

### 🧾 Contoh

Input:

```
[1, 2, 3, 4]
[3, 4, 5, 6]
```

Output:

```
[3, 4]
```

### ⏱ Kompleksitas

* Waktu: O(n + m)
* Ruang: O(n)

---

## 3️⃣ Anagram Check

### 🎯 Tujuan

Menentukan apakah dua string merupakan anagram.

### 💡 Konsep

Menggunakan `dictionary` untuk menghitung frekuensi karakter.

### 🧾 Contoh

```
listen & silent → True
hello & world → False
```

### ⏱ Kompleksitas

* Waktu: O(n)
* Ruang: O(n)

---

## 4️⃣ First Recurring Character

### 🎯 Tujuan

Menemukan karakter pertama yang muncul lebih dari sekali dalam string.

### 💡 Konsep

Menggunakan `set` untuk mendeteksi kemunculan ulang secara cepat.

### 🧾 Contoh

Input:

```
"abca"
```

Output:

```
"a"
```

Jika tidak ada karakter berulang:

```
None
```

### ⏱ Kompleksitas

* Waktu: O(n)
* Ruang: O(n)

---

## 5️⃣ Simulasi Buku Telepon (Phonebook)

### 🎯 Tujuan

Membuat program sederhana berbasis menu untuk:

* Menambah kontak
* Mencari kontak
* Menampilkan semua kontak

### 💡 Konsep

Menggunakan `dictionary` sebagai hash table dengan struktur:

```
nama → nomor_telepon
```

### 🔎 Kenapa Dictionary?

Karena:

* Pencarian nama sangat cepat (O(1))
* Struktur key-value sangat cocok untuk mapping data

### 🧾 Contoh Interaksi

```
1. Tambah Kontak
2. Cari Kontak
3. Tampilkan Semua
4. Keluar
```

### ⏱ Kompleksitas

* Tambah kontak: O(1)
* Cari kontak: O(1)
* Tampilkan semua: O(n)

---

# 🔍 Hubungan Antar Soal

Walaupun terlihat berbeda, semua soal memiliki fondasi yang sama:

| Soal            | Struktur Data | Prinsip Hash         |
| --------------- | ------------- | -------------------- |
| Deduplication   | Set           | Cek keberadaan cepat |
| Intersection    | Set           | Membership checking  |
| Anagram         | Dictionary    | Frequency counting   |
| First Recurring | Set           | Duplicate detection  |
| Phonebook       | Dictionary    | Key-value mapping    |

Semua berbasis hash table.

---

# 🚀 Cara Menjalankan

Pastikan Python sudah terinstall.

Jalankan file masing-masing:

```
python deduplication.py
python intersection.py
python anagram.py
python first_recurring.py
python phonebook.py
```

---

# 🎓 Kesimpulan

Latihan ini menunjukkan bahwa:

* Hashing membuat operasi pencarian sangat efisien.
* `set` dan `dict` adalah implementasi nyata dari hash table.
* Banyak permasalahan klasik dapat diselesaikan dengan pendekatan hashing.
* Struktur data yang tepat menentukan efisiensi algoritma.

Memahami konsep ini sangat penting sebelum mempelajari topik lanjutan seperti:

* Collision handling
* Linear probing
* Double hashing
* Separate chaining

---

# 📌 Author

Nama: M. Bagus Kuncoro Yekti
Mata Kuliah: Struktur Data
Semester: 2



Kamu ingin README ini sekadar cukup… atau sekalian dibuat terlihat seperti mahasiswa yang benar-benar paham konsep hashing?
