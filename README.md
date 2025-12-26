# 🛵 Sistem Delivery MakanCepat

## Final Project - Algorithm Foundations

Project ini mengimplementasikan tiga jenis algoritma fundamental:
- **Greedy Algorithm** (3 fitur)
- **Backtracking** (2 fitur)
- **Dynamic Programming** (2 fitur)

dalam konteks sistem delivery makanan online.

---

## 📁 Struktur File

```
makancepat_project/
├── README.md                      ← Dokumentasi (file ini)
├── main.py                        ← File utama (menu interaktif)
├── data_format.py                 ← Format data yang disepakati
│
├── fitur_a1_greedy.py             ← Greedy: Penjadwalan Time Window
├── fitur_a2_greedy.py             ← Greedy: Urutan Masak Optimal
├── fitur_a3_greedy_spbu.py        ← Greedy: Pengisian Bensin Efisien
│
├── fitur_b1_backtrack_rute.py     ← Backtracking: Generate Rute
├── fitur_b2_backtrack_promo.py    ← Backtracking: Kombinasi Promo
│
├── fitur_c1_dp_knapsack.py        ← DP: Optimasi Kapasitas Tas
└── fitur_c2_dp_topup.py           ← DP: Minimum Transaksi Top-up
```

---

## 🚀 Cara Menjalankan

### Menjalankan Program Utama (dengan Menu)

```bash
python main.py
```

Akan muncul menu interaktif untuk memilih fitur yang ingin dijalankan.

### Menjalankan Fitur Tertentu

```bash
# Jalankan fitur A.1 saja
python fitur_a1_greedy.py

# Jalankan fitur A.3 saja
python fitur_a3_greedy_spbu.py

# Jalankan fitur B.1 saja
python fitur_b1_backtrack_rute.py

# dst...
```

### Melihat Data Contoh

```bash
python data_format.py
```

---

## 📋 Deskripsi Fitur

### 🟢 GREEDY ALGORITHM

#### Fitur A.1: Penjadwalan Time Window

**Masalah:** Driver punya beberapa pesanan dengan waktu pickup dan deadline berbeda. Tentukan urutan pengiriman agar maksimal pesanan tepat waktu.

**Strategi:** Earliest Deadline First (EDF) - prioritaskan deadline terdekat.

**File:** `fitur_a1_greedy.py`

---

#### Fitur A.2: Urutan Masak Optimal

**Masalah:** Chef memasak satu per satu. Tentukan urutan masak agar total waktu tunggu driver minimal.

**Strategi:** Shortest Processing Time (SPT) - masak yang paling cepat dulu.

**File:** `fitur_a2_greedy.py`

---

#### Fitur A.3: Pengisian Bensin Efisien ⛽ (BARU)

**Masalah:** Driver harus isi bensin tapi tidak mau melenceng jauh dari rute pengantaran.

**Strategi:** Minimum Detour First - pilih SPBU dengan tambahan jarak terkecil.

**File:** `fitur_a3_greedy_spbu.py`

**Rumus Detour:**
```
detour = (jarak_driver→SPBU + jarak_SPBU→customer) - jarak_langsung
```

---

### 🔵 BACKTRACKING

#### Fitur B.1: Generate Semua Rute Valid

**Masalah:** Cari semua kemungkinan rute antar customer dengan constraint:
- Tidak boleh 3 zona sama berturut-turut
- Total jarak ≤ batas maksimal
- Minimal 2 zona berbeda dikunjungi

**Strategi:** Coba semua kombinasi, mundur (backtrack) jika tidak valid.

**File:** `fitur_b1_backtrack_rute.py`

---

#### Fitur B.2: Kombinasi Promo Valid

**Masalah:** Cari semua kombinasi promo yang bisa dipakai dengan constraint:
- Kategori dan syarat sesuai
- Maksimal 2 promo (stacking)
- Tidak boleh 2 promo dengan syarat sama
- Total diskon ≤ 50% dari total belanja

**Strategi:** Generate semua kombinasi 1-2 promo yang memenuhi syarat.

**File:** `fitur_b2_backtrack_promo.py`

---

### 🟣 DYNAMIC PROGRAMMING

#### Fitur C.1: Optimasi Kapasitas Tas (Knapsack)

**Masalah:** Tas delivery kapasitas terbatas. Pilih item dengan total tip maksimal.

**Strategi:** 0/1 Knapsack - buat tabel DP untuk menyimpan hasil optimal setiap sub-masalah.

**File:** `fitur_c1_dp_knapsack.py`

**Rekurens:**
```
dp[i][w] = max(dp[i-1][w], dp[i-1][w-volume] + tip)
```

---

#### Fitur C.2: Minimum Transaksi Top-up (Coin Change)

**Masalah:** Top-up saldo tepat N rupiah dengan minimum jumlah transaksi.

**Strategi:** Coin Change - untuk setiap saldo, cari kombinasi nominal dengan transaksi paling sedikit.

**File:** `fitur_c2_dp_topup.py`

**Rekurens:**
```
dp[saldo] = min(dp[saldo], dp[saldo-nominal] + 1)
```

---

## 📊 Format Data

Semua format data sudah disepakati di file `data_format.py`.

### Contoh Format Pesanan (Time Window)
```python
pesanan = {
    "id": "P1",
    "pickup": 0,      # waktu makanan siap
    "deadline": 5     # waktu harus sampai
}
```

### Contoh Format SPBU (Baru)
```python
spbu = {
    "id": "SPBU1",
    "nama": "SPBU Pertamina A",
    "x": 3,           # koordinat x
    "y": 2,           # koordinat y
    "harga": 13000    # harga per liter
}
```

### Contoh Format Customer
```python
customer = {
    "id": "C1",
    "nama": "Budi",
    "zona": "A",
    "jarak": 5        # dalam km
}
```

### Contoh Format Item Delivery
```python
item = {
    "id": "I1",
    "nama": "Nasi Goreng",
    "volume": 1500,   # dalam cm³
    "tip": 15000      # dalam rupiah
}
```

Lihat `data_format.py` untuk format lengkap.

---

## 🧮 Ringkasan Algoritma

| Fitur | Algoritma | Kompleksitas | Tujuan |
|-------|-----------|--------------|--------|
| A.1 | Greedy (EDF) | O(n log n) | Maksimalkan pesanan tepat waktu |
| A.2 | Greedy (SPT) | O(n log n) | Minimalkan total waktu tunggu |
| A.3 | Greedy (Min Detour) | O(n) | Minimalkan jarak tambahan |
| B.1 | Backtracking | O(n!) | Generate semua rute valid |
| B.2 | Backtracking | O(2^n) | Generate semua kombinasi promo |
| C.1 | DP Knapsack | O(n×W) | Maksimalkan tip dengan batasan volume |
| C.2 | DP Coin Change | O(n×S) | Minimalkan jumlah transaksi |

---

## 👥 Pembagian Tugas Kelompok

| Anggota | Fitur | Algoritma |
|---------|-------|-----------|
| [Herlangga] | A.1, A.2, A.3 | Greedy |
| [Fauzi,Chandra] | B.1, B.2 | Backtracking |
| [Nawwaf, Farid] | C.1, C.2 | Dynamic Programming |

---

## 📝 Catatan untuk Kelompok

1. **Jangan ubah format data** di `data_format.py` tanpa diskusi
2. **Test kode** sebelum digabung ke main.py
3. **Tambahkan komentar** yang jelas di setiap fungsi
4. Setiap file fitur bisa dijalankan **standalone** untuk testing

---

## ✅ Checklist Pengerjaan

- [x] Fitur A.1 - Penjadwalan Time Window
- [x] Fitur A.2 - Urutan Masak Optimal
- [x] Fitur A.3 - Pengisian Bensin Efisien (BARU)
- [x] Fitur B.1 - Generate Rute Valid
- [x] Fitur B.2 - Kombinasi Promo Valid
- [x] Fitur C.1 - Optimasi Kapasitas Tas
- [x] Fitur C.2 - Minimum Transaksi Top-up
- [x] Main menu interaktif
- [x] Data format disepakati
- [x] README dokumentasi

---

## 🎓 Dibuat untuk

**Final Project Mata Kuliah Algorithm Foundations**

Semester 1 - Program Studi Ilmu Komputer

---

## 📜 Lisensi

Project ini dibuat untuk keperluan akademik.
