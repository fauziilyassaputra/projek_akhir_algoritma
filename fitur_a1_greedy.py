# ============================================================
# FILE: fitur_a1_greedy.py
# FITUR: A.1 - Penjadwalan Pengiriman dengan Time Window
# ALGORITMA: GREEDY (Earliest Deadline First)
# ============================================================
# DIKERJAKAN OLEH: [NAMA ANGGOTA KELOMPOK]
# ============================================================

"""
DESKRIPSI MASALAH:
- Driver punya beberapa pesanan yang harus diantar
- Setiap pesanan punya:
  - pickup: waktu makanan siap diambil
  - deadline: waktu maksimal harus sampai ke customer
- Driver hanya bisa antar SATU pesanan dalam satu waktu
- Asumsi: setiap pengiriman membutuhkan 1 unit waktu
- Tujuan: Maksimalkan pesanan yang diantar TEPAT WAKTU

STRATEGI GREEDY - EARLIEST DEADLINE FIRST (EDF):
- Prioritaskan pesanan dengan deadline paling dekat
- Logika: yang deadline-nya mepet harus didahulukan

ANALOGI SEDERHANA:
- Seperti mengerjakan tugas kuliah
- Kerjakan tugas yang deadline-nya paling dekat dulu
- Tapi baru bisa dikerjakan kalau materinya sudah diajarkan (pickup)
"""

from typing import List, Dict, Tuple

# Tipe data untuk Pesanan (sesuai data_format.py)
Order = Dict[str, int | str]

# ============================================================
# IMPORT DATA FORMAT
# ============================================================
from data_format import CONTOH_PESANAN_TIMEWINDOW, print_pesanan_timewindow


# ============================================================
# FUNGSI UTAMA - GREEDY EARLIEST DEADLINE FIRST
# ============================================================

def penjadwalan_pengiriman_edf(
    orders: List[Order]
) -> Tuple[List[str], int, int, List[Dict]]:
    """
    Menentukan urutan pengiriman optimal menggunakan Earliest Deadline First.
    
    Args:
        orders: Daftar dictionary pesanan dengan key:
                - "id": string, ID pesanan
                - "pickup": integer, waktu makanan siap
                - "deadline": integer, batas waktu pengiriman
        
    Returns:
        Tuple berisi:
        - urutan_id: List ID pesanan dalam urutan optimal
        - jumlah_tepat_waktu: Jumlah pesanan yang tepat waktu
        - jumlah_terlambat: Jumlah pesanan yang terlambat
        - detail: List detail proses setiap pesanan
    """
    
    # LANGKAH 1: Sorting berdasarkan Deadline (Earliest First)
    # Jika deadline sama, prioritaskan yang pickup lebih awal
    sorted_orders = sorted(orders, key=lambda x: (x['deadline'], x['pickup']))
    
    # Variabel tracking
    current_time = 0  # Waktu saat ini
    urutan_id = []
    detail_proses = []
    jumlah_tepat_waktu = 0
    jumlah_terlambat = 0
    total_tardiness = 0  # Total keterlambatan
    
    # LANGKAH 2: Proses setiap pesanan berdasarkan urutan deadline
    for order in sorted_orders:
        id_pesanan = order['id']
        pickup = order['pickup']
        deadline = order['deadline']
        
        # Waktu mulai = max(waktu sekarang, waktu pickup)
        # Driver harus tunggu jika makanan belum siap
        start_time = max(current_time, pickup)
        
        # Waktu selesai (asumsi: 1 unit waktu untuk pengiriman)
        completion_time = start_time + 1
        
        # Update waktu sekarang
        current_time = completion_time
        
        # Cek keterlambatan (tardiness)
        tardiness = max(0, completion_time - deadline)
        total_tardiness += tardiness
        
        # Tentukan status
        if completion_time <= deadline:
            status = "TEPAT WAKTU"
            jumlah_tepat_waktu += 1
        else:
            status = f"TERLAMBAT (+{tardiness})"
            jumlah_terlambat += 1
        
        # Simpan hasil
        urutan_id.append(id_pesanan)
        detail_proses.append({
            "id": id_pesanan,
            "pickup": pickup,
            "deadline": deadline,
            "start_time": start_time,
            "completion_time": completion_time,
            "tardiness": tardiness,
            "status": status
        })
    
    return urutan_id, jumlah_tepat_waktu, jumlah_terlambat, detail_proses


# ============================================================
# FUNGSI UNTUK MENAMPILKAN HASIL
# ============================================================

def tampilkan_hasil(urutan, tepat_waktu, terlambat, detail):
    """Menampilkan hasil optimasi dengan format rapi"""
    
    print("\n" + "=" * 65)
    print("HASIL FITUR A.1: PENJADWALAN PENGIRIMAN TIME WINDOW")
    print("Algoritma: Greedy - Earliest Deadline First (EDF)")
    print("=" * 65)
    
    print("\n[URUTAN PENGIRIMAN OPTIMAL]")
    print(f"  {' -> '.join(urutan)}")
    
    print("\n[DETAIL PROSES PENGIRIMAN]")
    print(f"  {'ID':<5} {'Pickup':<8} {'Deadline':<10} {'Mulai':<8} {'Selesai':<9} {'Status'}")
    print("  " + "-" * 58)
    
    for d in detail:
        icon = "✓" if d['tardiness'] == 0 else "✗"
        print(f"  {d['id']:<5} {d['pickup']:<8} {d['deadline']:<10} "
              f"{d['start_time']:<8} {d['completion_time']:<9} {icon} {d['status']}")
    
    print("\n[RINGKASAN]")
    total = len(urutan)
    print(f"  Total pesanan   : {total}")
    print(f"  Tepat waktu     : {tepat_waktu} ({tepat_waktu/total*100:.1f}%)")
    print(f"  Terlambat       : {terlambat} ({terlambat/total*100:.1f}%)")
    print("=" * 65)


# ============================================================
# FUNGSI DENGAN PENJELASAN LANGKAH (untuk presentasi)
# ============================================================

def penjadwalan_dengan_penjelasan(orders: List[Order]):
    """Sama seperti fungsi utama, tapi dengan print penjelasan tiap langkah"""
    
    print("\n" + "-" * 65)
    print("PROSES ALGORITMA GREEDY - EARLIEST DEADLINE FIRST")
    print("-" * 65)
    
    print("\n[LANGKAH 1] Data pesanan awal:")
    for p in orders:
        print(f"  {p['id']}: pickup={p['pickup']}, deadline={p['deadline']}")
    
    # Sorting
    sorted_orders = sorted(orders, key=lambda x: (x['deadline'], x['pickup']))
    
    print("\n[LANGKAH 2] Setelah sorting berdasarkan deadline (terkecil dulu):")
    for p in sorted_orders:
        print(f"  {p['id']}: pickup={p['pickup']}, deadline={p['deadline']}")
    
    print("\n[LANGKAH 3] Simulasi pengiriman satu per satu:")
    
    current_time = 0
    urutan_id = []
    detail_proses = []
    jumlah_tepat_waktu = 0
    jumlah_terlambat = 0
    
    for i, order in enumerate(sorted_orders, 1):
        id_pesanan = order['id']
        pickup = order['pickup']
        deadline = order['deadline']
        
        print(f"\n  --- Pesanan ke-{i}: {id_pesanan} ---")
        print(f"  Waktu sekarang: t={current_time}")
        
        # Cek apakah perlu tunggu
        if current_time < pickup:
            print(f"  Makanan belum siap, tunggu sampai t={pickup}")
            current_time = pickup
        
        start_time = current_time
        completion_time = start_time + 1
        current_time = completion_time
        
        print(f"  Mulai antar di t={start_time}, selesai di t={completion_time}")
        
        tardiness = max(0, completion_time - deadline)
        
        if completion_time <= deadline:
            status = "TEPAT WAKTU"
            jumlah_tepat_waktu += 1
            print(f"  ✓ {status} (deadline: {deadline})")
        else:
            status = f"TERLAMBAT (+{tardiness})"
            jumlah_terlambat += 1
            print(f"  ✗ {status} (deadline: {deadline})")
        
        urutan_id.append(id_pesanan)
        detail_proses.append({
            "id": id_pesanan,
            "pickup": pickup,
            "deadline": deadline,
            "start_time": start_time,
            "completion_time": completion_time,
            "tardiness": tardiness,
            "status": status
        })
    
    return urutan_id, jumlah_tepat_waktu, jumlah_terlambat, detail_proses


# ============================================================
# MAIN - Testing
# ============================================================

if __name__ == "__main__":
    print("=" * 65)
    print("FITUR A.1: PENJADWALAN PENGIRIMAN DENGAN TIME WINDOW")
    print("Algoritma: GREEDY (Earliest Deadline First)")
    print("=" * 65)
    
    # Tampilkan data input dari data_format.py
    print_pesanan_timewindow(CONTOH_PESANAN_TIMEWINDOW)
    
    # Jalankan dengan penjelasan
    urutan, tepat_waktu, terlambat, detail = penjadwalan_dengan_penjelasan(
        CONTOH_PESANAN_TIMEWINDOW
    )
    
    # Tampilkan hasil
    tampilkan_hasil(urutan, tepat_waktu, terlambat, detail)
    
    # ============================================================
    # TEST DENGAN DATA BERBEDA
    # ============================================================
    print("\n\n" + "=" * 65)
    print("TEST DENGAN DATA BERBEDA (Ada yang terlambat)")
    print("=" * 65)
    
    pesanan_test = [
        {"id": "A", "pickup": 0, "deadline": 2},
        {"id": "B", "pickup": 0, "deadline": 3},
        {"id": "C", "pickup": 0, "deadline": 4},
        {"id": "D", "pickup": 0, "deadline": 2},  # Deadline sama dengan A
    ]
    
    print("\n[DATA TEST]")
    for p in pesanan_test:
        print(f"  {p['id']}: pickup={p['pickup']}, deadline={p['deadline']}")
    
    urutan2, tepat2, terlambat2, detail2 = penjadwalan_pengiriman_edf(pesanan_test)
    tampilkan_hasil(urutan2, tepat2, terlambat2, detail2)
    
    # ============================================================
    # TRACING MANUAL (untuk pemahaman)
    # ============================================================
    print("\n" + "=" * 65)
    print("TRACING MANUAL - CONTOH_PESANAN_TIMEWINDOW")
    print("=" * 65)
    print("""
Data awal:
  P1: pickup=0, deadline=5
  P2: pickup=2, deadline=8
  P3: pickup=1, deadline=4
  P4: pickup=3, deadline=7
  P5: pickup=4, deadline=10

Setelah sorting (deadline terkecil dulu):
  P3(d=4), P1(d=5), P4(d=7), P2(d=8), P5(d=10)

Simulasi:
  t=0: Ambil P3, tapi pickup=1, tunggu...
  t=1: Mulai antar P3, selesai t=2 ✓ (deadline 4)
  t=2: Ambil P1 (pickup=0, sudah siap), selesai t=3 ✓ (deadline 5)
  t=3: Ambil P4 (pickup=3, pas!), selesai t=4 ✓ (deadline 7)
  t=4: Ambil P2 (pickup=2, sudah siap), selesai t=5 ✓ (deadline 8)
  t=5: Ambil P5 (pickup=4, sudah siap), selesai t=6 ✓ (deadline 10)

Hasil: Semua 5 pesanan TEPAT WAKTU!
""")
