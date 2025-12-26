# ============================================================
# FILE: data_format.py
# DESKRIPSI: Format data yang DISEPAKATI KELOMPOK
# ============================================================
# PENTING: Semua anggota kelompok HARUS menggunakan format ini!
# Jangan mengubah nama key tanpa kesepakatan bersama!
# ============================================================

"""
CARA PAKAI FILE INI:
1. Semua anggota kelompok baca dan pahami format di bawah
2. Copy data contoh ke file masing-masing untuk testing
3. Kalau mau tambah field, diskusikan dulu di grup!
"""

# ============================================================
# FITUR A.1: PESANAN TIME WINDOW (Greedy)
# ============================================================
# Setiap pesanan HARUS punya 3 key ini:
#   - "id"       : string, ID unik pesanan (contoh: "P1", "P2")
#   - "pickup"   : integer, waktu makanan siap diambil
#   - "deadline" : integer, waktu maksimal harus sampai ke customer

CONTOH_PESANAN_TIMEWINDOW = [
    {"id": "P1", "pickup": 0, "deadline": 5},
    {"id": "P2", "pickup": 2, "deadline": 8},
    {"id": "P3", "pickup": 1, "deadline": 4},
    {"id": "P4", "pickup": 3, "deadline": 7},
    {"id": "P5", "pickup": 4, "deadline": 10},
]

# ============================================================
# FITUR A.2: PESANAN WAKTU MASAK (Greedy)
# ============================================================
# Setiap pesanan HARUS punya 2 key ini:
#   - "id"          : string, ID unik pesanan
#   - "waktu_masak" : integer, waktu yang dibutuhkan untuk memasak (dalam menit)

CONTOH_PESANAN_MASAK = [
    {"id": "P1", "waktu_masak": 12},
    {"id": "P2", "waktu_masak": 5},
    {"id": "P3", "waktu_masak": 8},
    {"id": "P4", "waktu_masak": 3},
    {"id": "P5", "waktu_masak": 15},
]

# ============================================================
# FITUR A.3: SPBU UNTUK PENGISIAN BENSIN (Greedy)
# ============================================================
# Posisi menggunakan koordinat (x, y) dalam satuan km dari titik origin

# Format POSISI DRIVER:
#   - "x" : integer/float, koordinat x
#   - "y" : integer/float, koordinat y

CONTOH_POSISI_DRIVER = {"x": 0, "y": 0}

# Format POSISI CUSTOMER:
#   - "id"   : string, ID customer
#   - "nama" : string, nama customer
#   - "x"    : integer/float, koordinat x
#   - "y"    : integer/float, koordinat y

CONTOH_POSISI_CUSTOMER = {
    "id": "C1",
    "nama": "Budi",
    "x": 10,
    "y": 8
}

# Format SPBU:
#   - "id"    : string, ID SPBU
#   - "nama"  : string, nama SPBU
#   - "x"     : integer/float, koordinat x
#   - "y"     : integer/float, koordinat y
#   - "harga" : integer, harga per liter (dalam rupiah)

CONTOH_DAFTAR_SPBU = [
    {"id": "SPBU1", "nama": "SPBU Pertamina A", "x": 3, "y": 2, "harga": 13000},
    {"id": "SPBU2", "nama": "SPBU Shell B", "x": 6, "y": 5, "harga": 14500},
    {"id": "SPBU3", "nama": "SPBU Pertamina C", "x": 2, "y": 7, "harga": 13000},
    {"id": "SPBU4", "nama": "SPBU BP D", "x": 8, "y": 3, "harga": 14000},
    {"id": "SPBU5", "nama": "SPBU Vivo E", "x": -2, "y": 4, "harga": 12500},
]

# ============================================================
# FITUR B.1: CUSTOMER UNTUK RUTE DELIVERY (Backtracking)
# ============================================================
# Setiap customer HARUS punya 4 key ini:
#   - "id"    : string, ID unik customer
#   - "nama"  : string, nama customer
#   - "zona"  : string, zona lokasi (contoh: "A", "B", "C")
#   - "jarak" : integer, jarak dari titik sebelumnya (dalam km)

CONTOH_CUSTOMERS = [
    {"id": "C1", "nama": "Budi", "zona": "A", "jarak": 5},
    {"id": "C2", "nama": "Ani", "zona": "B", "jarak": 3},
    {"id": "C3", "nama": "Citra", "zona": "A", "jarak": 4},
    {"id": "C4", "nama": "Dodi", "zona": "A", "jarak": 6},
]

# Constraint untuk Fitur B.1:
BATAS_JARAK_MAKSIMAL = 20  # dalam km

# ============================================================
# FITUR B.2: DATA PROMO (Backtracking)
# ============================================================
# Setiap promo HARUS punya 6 key ini:
#   - "id"            : string, ID unik promo
#   - "nama"          : string, nama promo
#   - "diskon"        : integer, nilai diskon (dalam rupiah)
#   - "kategori"      : string, kategori yang berlaku ("semua" = semua kategori)
#   - "min_pembelian" : integer, minimum total belanja untuk pakai promo
#   - "syarat"        : string, syarat khusus ("semua" = tanpa syarat khusus)

CONTOH_PROMO = [
    {
        "id": "PROMO1",
        "nama": "Diskon Weekend",
        "diskon": 10000,
        "kategori": "semua",
        "min_pembelian": 50000,
        "syarat": "weekend"
    },
    {
        "id": "PROMO2",
        "nama": "Diskon New User",
        "diskon": 15000,
        "kategori": "fast_food",
        "min_pembelian": 30000,
        "syarat": "new_user"
    },
    {
        "id": "PROMO3",
        "nama": "Diskon Minuman",
        "diskon": 5000,
        "kategori": "minuman",
        "min_pembelian": 20000,
        "syarat": "semua"
    },
    {
        "id": "PROMO4",
        "nama": "Cashback Weekend",
        "diskon": 8000,
        "kategori": "semua",
        "min_pembelian": 40000,
        "syarat": "weekend"
    },
    {
        "id": "PROMO5",
        "nama": "Promo Member",
        "diskon": 12000,
        "kategori": "fast_food",
        "min_pembelian": 60000,
        "syarat": "member"
    },
]

# Format KERANJANG BELANJA:
#   - "total"       : integer, total harga belanja
#   - "kategori"    : list of string, kategori item di keranjang
#   - "hari"        : string, hari saat checkout ("weekday" atau "weekend")
#   - "status_user" : string, status user ("new_user", "member", atau "regular")

CONTOH_KERANJANG = {
    "total": 80000,
    "kategori": ["fast_food", "minuman"],
    "hari": "weekend",
    "status_user": "new_user"
}

# ============================================================
# FITUR C.1: ITEM DELIVERY UNTUK TAS (Dynamic Programming)
# ============================================================
# Setiap item HARUS punya 4 key ini:
#   - "id"     : string, ID unik item
#   - "nama"   : string, nama item/makanan
#   - "volume" : integer, volume item (dalam cm3)
#   - "tip"    : integer, potensi tip dari customer (dalam rupiah)

CONTOH_ITEMS_DELIVERY = [
    {"id": "I1", "nama": "Nasi Goreng", "volume": 1500, "tip": 15000},
    {"id": "I2", "nama": "Burger", "volume": 2000, "tip": 20000},
    {"id": "I3", "nama": "Pizza", "volume": 3000, "tip": 25000},
    {"id": "I4", "nama": "Mie Ayam", "volume": 1000, "tip": 10000},
    {"id": "I5", "nama": "Soto", "volume": 2500, "tip": 18000},
]

# Constraint untuk Fitur C.1:
KAPASITAS_TAS = 6000  # dalam cm3

# ============================================================
# FITUR C.2: NOMINAL TOP-UP (Dynamic Programming)
# ============================================================
# Nominal top-up adalah list of integer (dalam rupiah)

CONTOH_NOMINAL_TOPUP = [10000, 20000, 25000, 50000, 100000]

# Target saldo yang ingin dicapai:
CONTOH_TARGET_SALDO = 75000

# ============================================================
# FUNGSI HELPER UNTUK PRINT DATA (OPSIONAL)
# ============================================================

def print_pesanan_timewindow(daftar_pesanan):
    """Menampilkan daftar pesanan time window dengan format rapi"""
    print("\n=== DAFTAR PESANAN (TIME WINDOW) ===")
    print(f"{'ID':<6} {'Pickup':<8} {'Deadline':<10}")
    print("-" * 26)
    for p in daftar_pesanan:
        print(f"{p['id']:<6} {p['pickup']:<8} {p['deadline']:<10}")
    print()

def print_pesanan_masak(daftar_pesanan):
    """Menampilkan daftar pesanan dengan waktu masak"""
    print("\n=== DAFTAR PESANAN (WAKTU MASAK) ===")
    print(f"{'ID':<6} {'Waktu Masak':<12}")
    print("-" * 20)
    for p in daftar_pesanan:
        print(f"{p['id']:<6} {p['waktu_masak']:<12} menit")
    print()

def print_spbu(daftar_spbu):
    """Menampilkan daftar SPBU"""
    print("\n=== DAFTAR SPBU ===")
    print(f"{'ID':<8} {'Nama':<20} {'Posisi':<12} {'Harga/L':<10}")
    print("-" * 52)
    for s in daftar_spbu:
        posisi = f"({s['x']}, {s['y']})"
        print(f"{s['id']:<8} {s['nama']:<20} {posisi:<12} Rp{s['harga']:,}")
    print()

def print_customers(daftar_customer):
    """Menampilkan daftar customer"""
    print("\n=== DAFTAR CUSTOMER ===")
    print(f"{'ID':<6} {'Nama':<10} {'Zona':<6} {'Jarak':<8}")
    print("-" * 32)
    for c in daftar_customer:
        print(f"{c['id']:<6} {c['nama']:<10} {c['zona']:<6} {c['jarak']:<8} km")
    print()

def print_promo(daftar_promo):
    """Menampilkan daftar promo"""
    print("\n=== DAFTAR PROMO ===")
    print(f"{'ID':<10} {'Nama':<20} {'Diskon':<10} {'Min.Beli':<12} {'Syarat':<10}")
    print("-" * 65)
    for p in daftar_promo:
        print(f"{p['id']:<10} {p['nama']:<20} Rp{p['diskon']:<8} Rp{p['min_pembelian']:<10} {p['syarat']:<10}")
    print()

def print_items_delivery(daftar_item):
    """Menampilkan daftar item delivery"""
    print("\n=== DAFTAR ITEM DELIVERY ===")
    print(f"{'ID':<6} {'Nama':<15} {'Volume':<12} {'Tip':<10}")
    print("-" * 45)
    for i in daftar_item:
        print(f"{i['id']:<6} {i['nama']:<15} {i['volume']:<12} cm3  Rp{i['tip']}")
    print()

# ============================================================
# TEST: Jalankan file ini untuk melihat semua contoh data
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("CONTOH DATA UNTUK PROJECT MAKANCEPAT")
    print("=" * 60)
    
    print_pesanan_timewindow(CONTOH_PESANAN_TIMEWINDOW)
    print_pesanan_masak(CONTOH_PESANAN_MASAK)
    print_spbu(CONTOH_DAFTAR_SPBU)
    print_customers(CONTOH_CUSTOMERS)
    print_promo(CONTOH_PROMO)
    print_items_delivery(CONTOH_ITEMS_DELIVERY)
    
    print(f"Posisi Driver: ({CONTOH_POSISI_DRIVER['x']}, {CONTOH_POSISI_DRIVER['y']})")
    print(f"Posisi Customer: {CONTOH_POSISI_CUSTOMER['nama']} di ({CONTOH_POSISI_CUSTOMER['x']}, {CONTOH_POSISI_CUSTOMER['y']})")
    print(f"Kapasitas Tas: {KAPASITAS_TAS} cm3")
    print(f"Batas Jarak: {BATAS_JARAK_MAKSIMAL} km")
    print(f"Nominal Top-up: {CONTOH_NOMINAL_TOPUP}")
    print(f"Target Saldo: Rp{CONTOH_TARGET_SALDO:,}")
