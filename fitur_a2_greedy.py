from typing import List, Dict, Tuple

# Tipe data untuk Pesanan
Order = Dict[str, int | str]

def urutan_masak_optimal_greedy(
    orders: List[Order]
) -> Tuple[List[str], int]:
    """
    Menentukan urutan memasak optimal untuk meminimalkan total waktu tunggu 
    menggunakan Algoritma Greedy (Shortest Processing Time First).
    
    Args:
        orders: Daftar dictionary pesanan (id, waktu_masak).
        
    Returns:
        Tuple: (Urutan ID pesanan optimal, Total waktu tunggu minimal)
    """
    
    # 1. Langkah Kunci Greedy: Sorting
    # Urutkan pesanan berdasarkan 'waktu_masak' (Shortest Processing Time) menaik.
    sorted_orders = sorted(orders, key=lambda order: order['waktu_masak'])
    
    optimal_order_ids: List[str] = []
    
    # 2. Perhitungan Waktu Tunggu
    total_waiting_time = 0
    current_completion_time = 0 # Waktu penyelesaian kumulatif (kapan pesanan siap)
    
    for order in sorted_orders:
        waktu_masak = order['waktu_masak']
        
        # Waktu driver tunggu = Waktu selesai pesanan sebelumnya (kumulatif) + waktu masak pesanan saat ini
        # Current_completion_time mencerminkan seberapa lama pesanan ini harus menunggu 
        # hingga dimulainya (setelah semua pesanan sebelumnya selesai).
        # Waktu penyelesaian (completion time) pesanan saat ini
        current_completion_time += waktu_masak
        
        # Waktu tunggu *pesanan ini* adalah waktu penyelesaiannya.
        # Waktu tunggu total adalah akumulasi dari waktu penyelesaian setiap pesanan.
        total_waiting_time += current_completion_time
        
        # Simpan ID pesanan untuk urutan output
        optimal_order_ids.append(order['id'])

    return optimal_order_ids, total_waiting_time

# ============================================================
# CONTOH DATA & EKSEKUSI
# ============================================================

CONTOH_PESANAN_MASAK: List[Order] = [
    {"id": "P1", "waktu_masak": 12},
    {"id": "P2", "waktu_masak": 5},
    {"id": "P3", "waktu_masak": 8},
    {"id": "P4", "waktu_masak": 3},
    {"id": "P5", "waktu_masak": 15},
]

# Jalankan fungsi
urutan_optimal, total_waktu = urutan_masak_optimal_greedy(CONTOH_PESANAN_MASAK)

# Tampilkan Hasil
print("--- HASIL OPTIMASI URUTAN MASAK (GREEDY) ---")
print(f"Strategi: Waktu Masak Terpendek (Shortest Processing Time First)")
print(f"Urutan Masak Optimal: **{urutan_optimal}**")
print(f"Total Waktu Tunggu Minimal Semua Driver: **{total_waktu} menit**")

# --- Penelusuran (Tracing) ---
# Pesanan terurut: P4(3), P2(5), P3(8), P1(12), P5(15)
# P4: Selesai di t=3. Total tunggu = 3
# P2: Selesai di t=3+5=8. Total tunggu = 3+8=11
# P3: Selesai di t=8+8=16. Total tunggu = 11+16=27
# P1: Selesai di t=16+12=28. Total tunggu = 27+28=55
# P5: Selesai di t=28+15=43. Total tunggu = 55+43=98
# Total Waktu Tunggu Minimal = 98 menit