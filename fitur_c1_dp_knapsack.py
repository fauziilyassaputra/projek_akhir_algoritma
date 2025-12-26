# ============================================================
# FILE: fitur_c1_dp_knapsack.py
# FITUR: C.1 - Optimasi Kapasitas Tas Delivery
# ALGORITMA: DYNAMIC PROGRAMMING (0/1 Knapsack)
# ============================================================
# DIKERJAKAN OLEH: [NAMA ANGGOTA KELOMPOK]
# ============================================================

"""
DESKRIPSI MASALAH:
- Driver punya tas dengan kapasitas terbatas (dalam cm³)
- Ada beberapa item/pesanan yang bisa diantar
- Setiap item punya:
  - volume: ukuran item (dalam cm³)
  - tip: potensi tip dari customer (dalam rupiah)
- Tujuan: Pilih item mana yang dibawa agar TOTAL TIP MAKSIMAL
  tanpa melebihi kapasitas tas

KONSEP KNAPSACK (0/1):
- Setiap item hanya bisa dipilih SEKALI (ambil atau tidak)
- Mirip seperti packing koper: pilih barang mana yang dibawa
  agar nilai maksimal tapi tidak over-kapasitas

STRATEGI DYNAMIC PROGRAMMING:
- Buat tabel dp[i][w] = tip maksimal dengan i item pertama dan kapasitas w
- Untuk setiap item, pilih: ambil atau tidak ambil
- dp[i][w] = max(tidak_ambil, ambil)
  - tidak_ambil = dp[i-1][w]
  - ambil = dp[i-1][w-volume] + tip (jika volume <= w)
"""

from typing import List, Dict, Tuple

# Tipe data untuk Item (sesuai data_format.py)
Item = Dict[str, int | str]

# ============================================================
# IMPORT DATA FORMAT
# ============================================================
from data_format import CONTOH_ITEMS_DELIVERY, KAPASITAS_TAS, print_items_delivery


# ============================================================
# FUNGSI UTAMA - DYNAMIC PROGRAMMING KNAPSACK
# ============================================================

def optimasi_kapasitas_tas(
    items: List[Item],
    kapasitas: int
) -> Tuple[int, List[Dict], List[List[int]]]:
    """
    Menentukan kombinasi item terbaik untuk tas delivery menggunakan
    algoritma Dynamic Programming (0/1 Knapsack).

    Parameter:
    - items: list of dict dengan key (sesuai data_format.py):
        - "id": string, ID item
        - "nama": string, nama item
        - "volume": integer, volume dalam cm³
        - "tip": integer, potensi tip dalam rupiah
    - kapasitas: integer, kapasitas tas dalam cm³

    Return:
    - total_tip_maksimal: integer
    - item_terpilih: list of dict (item yang dipilih)
    - tabel_dp: tabel DP untuk keperluan presentasi
    """

    n = len(items)

    # Buat tabel DP: dp[i][w] = tip maksimal dengan i item pertama dan kapasitas w
    # Ukuran: (n+1) x (kapasitas+1)
    dp = [[0] * (kapasitas + 1) for _ in range(n + 1)]

    # PROSES DP (BOTTOM-UP)
    for i in range(1, n + 1):
        volume = items[i - 1]["volume"]
        tip = items[i - 1]["tip"]

        for w in range(kapasitas + 1):
            # Opsi 1: Tidak ambil item ini
            tidak_ambil = dp[i - 1][w]
            
            # Opsi 2: Ambil item ini (jika muat)
            if volume <= w:
                ambil = dp[i - 1][w - volume] + tip
                dp[i][w] = max(tidak_ambil, ambil)
            else:
                dp[i][w] = tidak_ambil

    total_tip_maksimal = dp[n][kapasitas]

    # TRACEBACK - Cari item yang dipilih
    item_terpilih = []
    w = kapasitas

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            # Item ini dipilih
            item_terpilih.append(items[i - 1])
            w -= items[i - 1]["volume"]

    # Balik urutan agar sesuai urutan asli
    item_terpilih.reverse()

    return total_tip_maksimal, item_terpilih, dp


# ============================================================
# FUNGSI UNTUK MENAMPILKAN HASIL
# ============================================================

def tampilkan_hasil(total_tip, item_terpilih, kapasitas):
    """Menampilkan hasil optimasi dengan format rapi"""
    
    print("\n" + "=" * 60)
    print("HASIL FITUR C.1: OPTIMASI KAPASITAS TAS DELIVERY")
    print("Algoritma: Dynamic Programming (0/1 Knapsack)")
    print("=" * 60)
    
    print(f"\n[KAPASITAS TAS]")
    print(f"  Kapasitas maksimal: {kapasitas:,} cm³")
    
    print(f"\n[ITEM YANG DIPILIH]")
    if len(item_terpilih) == 0:
        print("  Tidak ada item yang bisa dimuat.")
    else:
        print(f"  {'ID':<5} {'Nama':<15} {'Volume':<12} {'Tip'}")
        print("  " + "-" * 45)
        
        for item in item_terpilih:
            print(f"  {item['id']:<5} {item['nama']:<15} {item['volume']:,} cm³      Rp{item['tip']:,}")
    
    # Hitung total volume
    total_volume = sum(item['volume'] for item in item_terpilih)
    sisa_kapasitas = kapasitas - total_volume
    
    print(f"\n[RINGKASAN]")
    print(f"  Jumlah item dipilih : {len(item_terpilih)}")
    print(f"  Total volume        : {total_volume:,} cm³")
    print(f"  Sisa kapasitas      : {sisa_kapasitas:,} cm³")
    print(f"  ━━━━━━━━━━━━━━━━━━━━")
    print(f"  TOTAL TIP MAKSIMAL  : Rp{total_tip:,}")
    print("=" * 60)


# ============================================================
# FUNGSI DENGAN PENJELASAN LANGKAH (untuk presentasi)
# ============================================================

def optimasi_dengan_penjelasan(items: List[Item], kapasitas: int):
    """Sama seperti fungsi utama, tapi dengan print penjelasan tiap langkah"""
    
    print("\n" + "-" * 60)
    print("PROSES ALGORITMA DYNAMIC PROGRAMMING - KNAPSACK")
    print("-" * 60)
    
    n = len(items)
    
    print(f"\n[LANGKAH 1] Data item yang tersedia:")
    for item in items:
        print(f"  {item['id']}: {item['nama']} | Volume: {item['volume']:,} cm³ | Tip: Rp{item['tip']:,}")
    print(f"\n  Kapasitas tas: {kapasitas:,} cm³")
    
    print(f"\n[LANGKAH 2] Membangun tabel DP...")
    print("  dp[i][w] = tip maksimal dengan i item pertama dan kapasitas w")
    print("  Untuk setiap item, pilih: AMBIL atau TIDAK AMBIL")
    
    # Buat tabel DP
    dp = [[0] * (kapasitas + 1) for _ in range(n + 1)]
    
    # Isi tabel DP dengan penjelasan
    for i in range(1, n + 1):
        item = items[i - 1]
        volume = item["volume"]
        tip = item["tip"]
        
        print(f"\n  --- Item ke-{i}: {item['nama']} (volume={volume:,}, tip=Rp{tip:,}) ---")
        
        for w in range(kapasitas + 1):
            tidak_ambil = dp[i - 1][w]
            
            if volume <= w:
                ambil = dp[i - 1][w - volume] + tip
                dp[i][w] = max(tidak_ambil, ambil)
                
                # Hanya print untuk kapasitas maksimal (agar tidak terlalu panjang)
                if w == kapasitas:
                    keputusan = "AMBIL" if dp[i][w] == ambil else "TIDAK AMBIL"
                    print(f"  Kapasitas {w:,}: tidak_ambil=Rp{tidak_ambil:,}, ambil=Rp{ambil:,}")
                    print(f"  → Pilih: {keputusan} → dp[{i}][{w}] = Rp{dp[i][w]:,}")
            else:
                dp[i][w] = tidak_ambil
                if w == kapasitas:
                    print(f"  Kapasitas {w:,}: volume {volume:,} > kapasitas → TIDAK MUAT")
                    print(f"  → dp[{i}][{w}] = Rp{dp[i][w]:,}")
    
    print(f"\n[LANGKAH 3] Backtracking untuk cari item terpilih...")
    
    item_terpilih = []
    w = kapasitas
    
    for i in range(n, 0, -1):
        item = items[i - 1]
        if dp[i][w] != dp[i - 1][w]:
            print(f"  ✓ {item['nama']} DIPILIH (volume={item['volume']:,})")
            item_terpilih.append(item)
            w -= item["volume"]
        else:
            print(f"  ✗ {item['nama']} tidak dipilih")
    
    item_terpilih.reverse()
    total_tip = dp[n][kapasitas]
    
    return total_tip, item_terpilih, dp


# ============================================================
# FUNGSI UNTUK PRINT TABEL DP (untuk data kecil)
# ============================================================

def print_tabel_dp_kecil(dp, items, kapasitas):
    """Print tabel DP untuk data dengan kapasitas kecil"""
    
    n = len(items)
    
    print("\n[TABEL DP LENGKAP]")
    
    # Header
    header = "Item".ljust(12)
    for w in range(kapasitas + 1):
        header += f"w={w}".rjust(6)
    print(header)
    print("-" * len(header))
    
    # Baris
    for i in range(n + 1):
        if i == 0:
            nama = "(none)"
        else:
            nama = items[i - 1]['id']
        
        baris = nama.ljust(12)
        for w in range(kapasitas + 1):
            baris += f"{dp[i][w]}".rjust(6)
        print(baris)


# ============================================================
# MAIN - Testing
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("FITUR C.1: OPTIMASI KAPASITAS TAS DELIVERY")
    print("Algoritma: DYNAMIC PROGRAMMING (0/1 Knapsack)")
    print("=" * 60)
    
    # Tampilkan data input dari data_format.py
    print_items_delivery(CONTOH_ITEMS_DELIVERY)
    print(f"Kapasitas Tas: {KAPASITAS_TAS:,} cm³")
    
    # Jalankan dengan penjelasan
    total_tip, item_terpilih, tabel_dp = optimasi_dengan_penjelasan(
        CONTOH_ITEMS_DELIVERY, 
        KAPASITAS_TAS
    )
    
    # Tampilkan hasil
    tampilkan_hasil(total_tip, item_terpilih, KAPASITAS_TAS)
    
    # ============================================================
    # TEST DENGAN KAPASITAS BERBEDA
    # ============================================================
    print("\n\n" + "=" * 60)
    print("TEST DENGAN KAPASITAS BERBEDA")
    print("=" * 60)
    
    kapasitas_test = 4000
    print(f"\nKapasitas tas: {kapasitas_test:,} cm³")
    
    total_tip2, item_terpilih2, _ = optimasi_kapasitas_tas(
        CONTOH_ITEMS_DELIVERY, 
        kapasitas_test
    )
    tampilkan_hasil(total_tip2, item_terpilih2, kapasitas_test)
    
    # ============================================================
    # TEST DENGAN DATA KECIL (untuk lihat tabel DP lengkap)
    # ============================================================
    print("\n\n" + "=" * 60)
    print("TEST DENGAN DATA KECIL (untuk lihat tabel DP)")
    print("=" * 60)
    
    item_kecil = [
        {"id": "A", "nama": "Item A", "volume": 2, "tip": 3},
        {"id": "B", "nama": "Item B", "volume": 3, "tip": 4},
        {"id": "C", "nama": "Item C", "volume": 4, "tip": 5},
    ]
    kapasitas_kecil = 6
    
    print("\n[DATA TEST]")
    for item in item_kecil:
        print(f"  {item['id']}: volume={item['volume']}, tip={item['tip']}")
    print(f"  Kapasitas: {kapasitas_kecil}")
    
    total_tip3, item_terpilih3, dp_kecil = optimasi_kapasitas_tas(
        item_kecil, 
        kapasitas_kecil
    )
    
    # Print tabel DP lengkap
    print_tabel_dp_kecil(dp_kecil, item_kecil, kapasitas_kecil)
    
    print(f"\nItem terpilih: {[item['id'] for item in item_terpilih3]}")
    print(f"Total tip: {total_tip3}")
    
    # ============================================================
    # TRACING MANUAL (untuk pemahaman)
    # ============================================================
    print("\n" + "=" * 60)
    print("TRACING MANUAL - CONTOH_ITEMS_DELIVERY")
    print("=" * 60)
    print("""
Data:
  I1: Nasi Goreng | volume=1500 | tip=15000
  I2: Burger      | volume=2000 | tip=20000
  I3: Pizza       | volume=3000 | tip=25000
  I4: Mie Ayam    | volume=1000 | tip=10000
  I5: Soto        | volume=2500 | tip=18000
  
Kapasitas tas: 6000 cm³

Proses DP (hanya untuk w=6000):
  i=1 (Nasi Goreng): ambil=15000, tidak=0 → AMBIL → dp=15000
  i=2 (Burger): ambil=35000, tidak=15000 → AMBIL → dp=35000
  i=3 (Pizza): ambil=45000, tidak=35000 → AMBIL → dp=45000
  i=4 (Mie Ayam): ambil=55000, tidak=45000 → AMBIL → dp=55000
  i=5 (Soto): ambil=53000, tidak=55000 → TIDAK → dp=55000

Backtrack:
  i=5: dp[5][6000]=55000 == dp[4][6000]=55000 → Soto TIDAK dipilih
  i=4: dp[4][6000]=55000 != dp[3][6000]=45000 → Mie Ayam DIPILIH, w=5000
  i=3: dp[3][5000]=45000 != dp[2][5000]=35000 → Pizza DIPILIH, w=2000
  i=2: dp[2][2000]=20000 != dp[1][2000]=0 → Burger DIPILIH, w=0
  i=1: w=0, stop

Hasil: Burger + Pizza + Mie Ayam
Volume: 2000 + 3000 + 1000 = 6000 cm³ (pas!)
Total Tip: 20000 + 25000 + 10000 = Rp55.000
""")
