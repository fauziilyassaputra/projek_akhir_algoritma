# ============================================================
# FILE: fitur_b2_backtrack_promo.py
# FITUR: B.2 - Generate Semua Kombinasi Promo Valid
# ALGORITMA: BACKTRACKING
# ============================================================
# DIKERJAKAN OLEH: [NAMA ANGGOTA KELOMPOK]
# ============================================================

"""
DESKRIPSI MASALAH:
- Customer ingin melihat semua promo yang bisa dipakai
- Aturan/constraint:
  1. Promo hanya berlaku jika kategori sesuai (atau "semua")
  2. Harus memenuhi minimum pembelian
  3. Maksimal 2 promo yang bisa di-stack
  4. Tidak boleh 2 promo dengan syarat yang sama (misal 2 promo weekend)
  5. Total diskon tidak melebihi 50% dari total belanja

TUJUAN: Generate SEMUA kombinasi promo yang VALID (1 atau 2 promo)

KONSEP BACKTRACKING:
- Coba setiap promo
- Cek apakah valid untuk keranjang ini
- Kalau bisa stack, coba kombinasikan dengan promo lain
- Mundur dan coba kombinasi lain
"""

# ============================================================
# IMPORT DATA FORMAT (untuk testing)
# ============================================================
from data_format import CONTOH_PROMO, CONTOH_KERANJANG, print_promo


# ============================================================
# FUNGSI HELPER
# ============================================================

def cek_promo_berlaku(promo, keranjang):
    """
    Mengecek apakah sebuah promo bisa dipakai untuk keranjang ini.
    
    Cek:
    1. Kategori promo sesuai dengan kategori di keranjang
    2. Total belanja memenuhi minimum pembelian
    3. Syarat promo terpenuhi (hari/status user)
    
    Parameter:
    - promo: dict (data satu promo)
    - keranjang: dict (data keranjang belanja)
    
    Return:
    - True jika promo bisa dipakai
    - False jika tidak bisa
    """
    
    # Cek 1: Kategori sesuai
    # Promo berlaku jika kategori = "semua" ATAU kategori ada di keranjang
    if promo["kategori"] != "semua":
        if promo["kategori"] not in keranjang["kategori"]:
            return False
    
    # Cek 2: Minimum pembelian
    if keranjang["total"] < promo["min_pembelian"]:
        return False
    
    # Cek 3: Syarat khusus
    # Syarat = "semua" berarti tidak ada syarat khusus
    if promo["syarat"] != "semua":
        # Cek hari
        if promo["syarat"] == "weekend":
            if keranjang["hari"] != "weekend":
                return False
        elif promo["syarat"] == "weekday":
            if keranjang["hari"] != "weekday":
                return False
        # Cek status user
        elif promo["syarat"] == "new_user":
            if keranjang["status_user"] != "new_user":
                return False
        elif promo["syarat"] == "member":
            if keranjang["status_user"] != "member":
                return False
    
    return True


def cek_syarat_bentrok(kombinasi_sekarang, promo_baru):
    """
    Mengecek apakah promo baru punya syarat yang sama dengan promo di kombinasi.
    
    Parameter:
    - kombinasi_sekarang: list of dict (promo yang sudah dipilih)
    - promo_baru: dict (promo yang mau ditambahkan)
    
    Return:
    - True jika BENTROK (syarat sama)
    - False jika tidak bentrok (aman)
    """
    
    # Kalau syarat promo baru adalah "semua", tidak akan bentrok
    if promo_baru["syarat"] == "semua":
        return False
    
    # Cek apakah ada promo di kombinasi dengan syarat yang sama
    for promo in kombinasi_sekarang:
        if promo["syarat"] == promo_baru["syarat"]:
            return True  # BENTROK!
    
    return False


# ============================================================
# FUNGSI UTAMA - BACKTRACKING
# ============================================================

def cari_kombinasi_promo(daftar_promo, keranjang):
    """
    Mencari semua kombinasi promo valid menggunakan backtracking.
    
    Parameter:
    - daftar_promo: list of dict, semua promo yang tersedia
    - keranjang: dict, data keranjang belanja
    
    Return:
    - list of dict: semua kombinasi valid
      Setiap dict berisi: {"promo": [...], "total_diskon": int, "persen_diskon": float}
    """
    
    hasil = []
    
    # LANGKAH 1: Filter promo yang applicable untuk keranjang ini
    promo_valid = []
    for promo in daftar_promo:
        if cek_promo_berlaku(promo, keranjang):
            promo_valid.append(promo)
    
    # Batas maksimal diskon = 50% dari total belanja
    batas_diskon = keranjang["total"] * 0.5
    
    def backtrack(index, kombinasi, total_diskon):
        """
        Fungsi rekursif untuk backtracking.
        
        Parameter:
        - index: integer, mulai dari promo ke berapa
        - kombinasi: list, kombinasi promo yang sedang dibangun
        - total_diskon: integer, total diskon sejauh ini
        """
        
        # Simpan kombinasi kalau tidak kosong dan valid
        if len(kombinasi) > 0 and total_diskon <= batas_diskon:
            persen = (total_diskon / keranjang["total"]) * 100
            hasil.append({
                "promo": [p["id"] for p in kombinasi],
                "nama_promo": [p["nama"] for p in kombinasi],
                "total_diskon": total_diskon,
                "persen_diskon": round(persen, 1)
            })
        
        # CONSTRAINT: Maksimal 2 promo
        if len(kombinasi) >= 2:
            return
        
        # Coba tambah promo lain
        for i in range(index, len(promo_valid)):
            promo = promo_valid[i]
            diskon_baru = total_diskon + promo["diskon"]
            
            # CEK CONSTRAINT: Total diskon tidak melebihi 50%
            if diskon_baru > batas_diskon:
                continue
            
            # CEK CONSTRAINT: Tidak boleh syarat yang sama
            if cek_syarat_bentrok(kombinasi, promo):
                continue
            
            # PILIH
            kombinasi.append(promo)
            
            # EXPLORE (i+1 agar tidak mengulang promo yang sama)
            backtrack(i + 1, kombinasi, diskon_baru)
            
            # BACKTRACK
            kombinasi.pop()
    
    # Mulai backtracking
    backtrack(0, [], 0)
    
    return hasil, promo_valid


# ============================================================
# FUNGSI UNTUK MENAMPILKAN HASIL
# ============================================================

def tampilkan_hasil(hasil, promo_valid, keranjang):
    """Menampilkan semua kombinasi promo valid dengan format rapi"""
    print("\n" + "=" * 60)
    print("HASIL FITUR B.2: KOMBINASI PROMO VALID")
    print("=" * 60)
    
    print(f"\n[DATA KERANJANG]")
    print(f"  Total belanja: Rp{keranjang['total']:,}")
    print(f"  Kategori: {keranjang['kategori']}")
    print(f"  Hari: {keranjang['hari']}")
    print(f"  Status: {keranjang['status_user']}")
    print(f"  Batas diskon (50%): Rp{int(keranjang['total'] * 0.5):,}")
    
    print(f"\n[PROMO YANG APPLICABLE]")
    if len(promo_valid) == 0:
        print("  Tidak ada promo yang bisa dipakai.")
    else:
        for p in promo_valid:
            print(f"  - {p['id']}: {p['nama']} (Rp{p['diskon']:,})")
    
    print(f"\n[KOMBINASI VALID]")
    if len(hasil) == 0:
        print("  Tidak ada kombinasi promo yang valid.")
    else:
        # Pisahkan kombinasi 1 promo dan 2 promo
        satu_promo = [h for h in hasil if len(h["promo"]) == 1]
        dua_promo = [h for h in hasil if len(h["promo"]) == 2]
        
        if len(satu_promo) > 0:
            print("\n  --- 1 PROMO ---")
            for i, h in enumerate(satu_promo, 1):
                nama = h["nama_promo"][0]
                print(f"  {i}. {nama}")
                print(f"     Diskon: Rp{h['total_diskon']:,} ({h['persen_diskon']}%)")
        
        if len(dua_promo) > 0:
            print("\n  --- 2 PROMO (STACKING) ---")
            for i, h in enumerate(dua_promo, 1):
                nama1 = h["nama_promo"][0]
                nama2 = h["nama_promo"][1]
                print(f"  {i}. {nama1} + {nama2}")
                print(f"     Diskon: Rp{h['total_diskon']:,} ({h['persen_diskon']}%)")
    
    print(f"\nTotal kombinasi ditemukan: {len(hasil)}")
    print("=" * 60)


# ============================================================
# FUNGSI DENGAN PENJELASAN (untuk presentasi)
# ============================================================

def cari_promo_dengan_penjelasan(daftar_promo, keranjang):
    """
    Sama seperti cari_kombinasi_promo, tapi dengan print penjelasan.
    """
    
    print("\n" + "-" * 60)
    print("PROSES ALGORITMA BACKTRACKING - KOMBINASI PROMO")
    print("-" * 60)
    
    print("\n[LANGKAH 1] Filter promo yang applicable:")
    promo_valid = []
    for promo in daftar_promo:
        berlaku = cek_promo_berlaku(promo, keranjang)
        status = "✓ BERLAKU" if berlaku else "✗ TIDAK"
        print(f"  {promo['id']}: {status}")
        if berlaku:
            promo_valid.append(promo)
    
    print(f"\nPromo yang bisa dipakai: {[p['id'] for p in promo_valid]}")
    
    hasil = []
    batas_diskon = keranjang["total"] * 0.5
    
    print(f"\n[LANGKAH 2] Generate kombinasi (max diskon: Rp{int(batas_diskon):,}):")
    
    def backtrack(index, kombinasi, total_diskon, level):
        indent = "  " * level
        
        if len(kombinasi) > 0 and total_diskon <= batas_diskon:
            combo_str = " + ".join([p["id"] for p in kombinasi])
            print(f"{indent}→ Kombinasi valid: [{combo_str}] = Rp{total_diskon:,}")
            hasil.append({
                "promo": [p["id"] for p in kombinasi],
                "nama_promo": [p["nama"] for p in kombinasi],
                "total_diskon": total_diskon,
                "persen_diskon": round((total_diskon / keranjang["total"]) * 100, 1)
            })
        
        if len(kombinasi) >= 2:
            return
        
        for i in range(index, len(promo_valid)):
            promo = promo_valid[i]
            diskon_baru = total_diskon + promo["diskon"]
            
            if diskon_baru > batas_diskon:
                print(f"{indent}  Coba {promo['id']}: ✗ Diskon {diskon_baru:,} > batas")
                continue
            
            if cek_syarat_bentrok(kombinasi, promo):
                print(f"{indent}  Coba {promo['id']}: ✗ Syarat '{promo['syarat']}' sudah ada")
                continue
            
            print(f"{indent}  Coba {promo['id']}: OK")
            kombinasi.append(promo)
            backtrack(i + 1, kombinasi, diskon_baru, level + 1)
            kombinasi.pop()
    
    backtrack(0, [], 0, 1)
    
    return hasil, promo_valid


# ============================================================
# MAIN - Testing
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("FITUR B.2: GENERATE SEMUA KOMBINASI PROMO VALID")
    print("Algoritma: BACKTRACKING")
    print("=" * 60)
    
    # Tampilkan data input
    print_promo(CONTOH_PROMO)
    
    print("\n[DATA KERANJANG]")
    print(f"  Total: Rp{CONTOH_KERANJANG['total']:,}")
    print(f"  Kategori: {CONTOH_KERANJANG['kategori']}")
    print(f"  Hari: {CONTOH_KERANJANG['hari']}")
    print(f"  Status: {CONTOH_KERANJANG['status_user']}")
    
    # Jalankan algoritma dengan penjelasan
    hasil, promo_valid = cari_promo_dengan_penjelasan(CONTOH_PROMO, CONTOH_KERANJANG)
    
    # Tampilkan hasil
    tampilkan_hasil(hasil, promo_valid, CONTOH_KERANJANG)
    
    # Test dengan keranjang berbeda
    print("\n\n" + "=" * 60)
    print("TEST DENGAN KERANJANG BERBEDA")
    print("=" * 60)
    
    keranjang_test = {
        "total": 100000,
        "kategori": ["fast_food"],
        "hari": "weekday",
        "status_user": "member"
    }
    
    print("\n[KERANJANG TEST]")
    print(f"  Total: Rp{keranjang_test['total']:,}")
    print(f"  Kategori: {keranjang_test['kategori']}")
    print(f"  Hari: {keranjang_test['hari']}")
    print(f"  Status: {keranjang_test['status_user']}")
    
    hasil2, valid2 = cari_kombinasi_promo(CONTOH_PROMO, keranjang_test)
    tampilkan_hasil(hasil2, valid2, keranjang_test)
