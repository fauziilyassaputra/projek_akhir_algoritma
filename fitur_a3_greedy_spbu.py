# ============================================================
# FILE: fitur_a3_greedy_spbu.py
# FITUR: A.3 - Pengisian Bensin Efisien (Gas Station Routing)
# ALGORITMA: GREEDY (Minimum Detour First)
# ============================================================

import math

# ============================================================
# FUNGSI UTAMA
# ============================================================

def hitung_jarak(pos1, pos2):
    """Menghitung jarak Euclidean antara dua titik"""
    dx = pos2["x"] - pos1["x"]
    dy = pos2["y"] - pos1["y"]
    return math.sqrt(dx**2 + dy**2)


def pilih_spbu_optimal(pos_driver, pos_customer, daftar_spbu):
    """
    Memilih SPBU dengan detour terkecil (Greedy).
    
    Detour = (jarak driver->SPBU + jarak SPBU->customer) - jarak langsung
    """
    
    jarak_langsung = hitung_jarak(pos_driver, pos_customer)
    
    # Hitung detour untuk setiap SPBU
    hasil_spbu = []
    for spbu in daftar_spbu:
        jarak_ke_spbu = hitung_jarak(pos_driver, spbu)
        jarak_ke_customer = hitung_jarak(spbu, pos_customer)
        jarak_total = jarak_ke_spbu + jarak_ke_customer
        detour = jarak_total - jarak_langsung
        
        hasil_spbu.append({
            "spbu": spbu,
            "jarak_total": jarak_total,
            "detour": detour
        })
    
    # GREEDY: Pilih detour terkecil
    hasil_spbu.sort(key=lambda x: x["detour"])
    
    return hasil_spbu, jarak_langsung


# ============================================================
# CONTOH DATA
# ============================================================

POSISI_DRIVER = {"x": 0, "y": 0}

POSISI_CUSTOMER = {"id": "C1", "nama": "Budi", "x": 10, "y": 8}

DAFTAR_SPBU = [
    {"id": "SPBU1", "nama": "SPBU Pertamina A", "x": 3, "y": 2, "harga": 13000},
    {"id": "SPBU2", "nama": "SPBU Shell B", "x": 6, "y": 5, "harga": 14500},
    {"id": "SPBU3", "nama": "SPBU Pertamina C", "x": 2, "y": 7, "harga": 13000},
    {"id": "SPBU4", "nama": "SPBU BP D", "x": 8, "y": 3, "harga": 14000},
    {"id": "SPBU5", "nama": "SPBU Vivo E", "x": -2, "y": 4, "harga": 12500},
]


# ============================================================
# EKSEKUSI
# ============================================================

hasil, jarak_langsung = pilih_spbu_optimal(POSISI_DRIVER, POSISI_CUSTOMER, DAFTAR_SPBU)

# Tampilkan hasil
print("=== HASIL PEMILIHAN SPBU (GREEDY) ===")
print(f"Jarak langsung ke customer: {jarak_langsung:.2f} km\n")

print("Ranking SPBU (detour terkecil):")
for i, h in enumerate(hasil, 1):
    spbu = h["spbu"]
    print(f"  {i}. {spbu['nama']} | Jarak: {h['jarak_total']:.2f} km | Detour: +{h['detour']:.2f} km")

print(f"\n✓ SPBU Terpilih: {hasil[0]['spbu']['nama']}")
print(f"  Detour: +{hasil[0]['detour']:.2f} km")