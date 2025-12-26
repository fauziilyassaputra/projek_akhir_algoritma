# ============================================================
# FILE: main.py
# DESKRIPSI: Menu Utama Sistem Delivery MakanCepat
# ============================================================
# Jalankan file ini untuk mengakses semua fitur
# ============================================================

import math

# ============================================================
# IMPORT DATA
# ============================================================
from data_format import (
    CONTOH_PESANAN_TIMEWINDOW,
    CONTOH_PESANAN_MASAK,
    CONTOH_POSISI_DRIVER,
    CONTOH_POSISI_CUSTOMER,
    CONTOH_DAFTAR_SPBU,
    CONTOH_CUSTOMERS,
    BATAS_JARAK_MAKSIMAL,
    CONTOH_PROMO,
    CONTOH_KERANJANG,
    CONTOH_ITEMS_DELIVERY,
    KAPASITAS_TAS,
    CONTOH_NOMINAL_TOPUP,
    CONTOH_TARGET_SALDO
)

# ============================================================
# FITUR A.1: GREEDY - EARLIEST DEADLINE FIRST
# ============================================================
def fitur_a1_timewindow():
    """Penjadwalan pengiriman dengan time window"""
    print("\n" + "=" * 60)
    print("FITUR A.1: PENJADWALAN PENGIRIMAN (TIME WINDOW)")
    print("Algoritma: Greedy - Earliest Deadline First")
    print("=" * 60)
    
    orders = CONTOH_PESANAN_TIMEWINDOW
    
    print("\n[DATA INPUT]")
    for p in orders:
        print(f"  {p['id']}: pickup={p['pickup']}, deadline={p['deadline']}")
    
    # Sorting berdasarkan deadline
    sorted_orders = sorted(orders, key=lambda x: (x['deadline'], x['pickup']))
    
    print("\n[PROSES] Urutkan berdasarkan deadline terkecil:")
    for p in sorted_orders:
        print(f"  {p['id']}: deadline={p['deadline']}")
    
    # Simulasi
    current_time = 0
    hasil = []
    
    print("\n[SIMULASI PENGIRIMAN]")
    for order in sorted_orders:
        start_time = max(current_time, order['pickup'])
        completion_time = start_time + 1
        current_time = completion_time
        
        status = "TEPAT WAKTU" if completion_time <= order['deadline'] else "TERLAMBAT"
        hasil.append({"id": order['id'], "selesai": completion_time, "status": status})
        print(f"  {order['id']}: mulai t={start_time}, selesai t={completion_time} -> {status}")
    
    tepat_waktu = sum(1 for h in hasil if h['status'] == "TEPAT WAKTU")
    print(f"\n[HASIL] {tepat_waktu}/{len(hasil)} pesanan tepat waktu")


# ============================================================
# FITUR A.2: GREEDY - SHORTEST PROCESSING TIME
# ============================================================
def fitur_a2_masak():
    """Optimasi urutan masak"""
    print("\n" + "=" * 60)
    print("FITUR A.2: OPTIMASI URUTAN MASAK")
    print("Algoritma: Greedy - Shortest Processing Time First")
    print("=" * 60)
    
    orders = CONTOH_PESANAN_MASAK
    
    print("\n[DATA INPUT]")
    for p in orders:
        print(f"  {p['id']}: waktu_masak={p['waktu_masak']} menit")
    
    # Sorting berdasarkan waktu masak
    sorted_orders = sorted(orders, key=lambda x: x['waktu_masak'])
    
    print("\n[PROSES] Urutkan berdasarkan waktu masak terpendek:")
    urutan = [p['id'] for p in sorted_orders]
    print(f"  Urutan: {urutan}")
    
    # Hitung total waktu tunggu
    total_tunggu = 0
    waktu_kumulatif = 0
    
    print("\n[PERHITUNGAN WAKTU TUNGGU]")
    for order in sorted_orders:
        waktu_kumulatif += order['waktu_masak']
        total_tunggu += waktu_kumulatif
        print(f"  {order['id']}: selesai di t={waktu_kumulatif}, total tunggu = {total_tunggu}")
    
    print(f"\n[HASIL] Total waktu tunggu minimal: {total_tunggu} menit")


# ============================================================
# FITUR A.3: GREEDY - MINIMUM DETOUR (SPBU)
# ============================================================
def fitur_a3_spbu():
    """Pemilihan SPBU dengan detour terkecil"""
    print("\n" + "=" * 60)
    print("FITUR A.3: PENGISIAN BENSIN EFISIEN")
    print("Algoritma: Greedy - Minimum Detour First")
    print("=" * 60)
    
    driver = CONTOH_POSISI_DRIVER
    customer = CONTOH_POSISI_CUSTOMER
    spbu_list = CONTOH_DAFTAR_SPBU
    
    print(f"\n[DATA INPUT]")
    print(f"  Posisi Driver  : ({driver['x']}, {driver['y']})")
    print(f"  Posisi Customer: {customer['nama']} di ({customer['x']}, {customer['y']})")
    print(f"  Jumlah SPBU    : {len(spbu_list)}")
    
    # Hitung jarak langsung
    def hitung_jarak(p1, p2):
        return math.sqrt((p2['x']-p1['x'])**2 + (p2['y']-p1['y'])**2)
    
    jarak_langsung = hitung_jarak(driver, customer)
    print(f"\n  Jarak langsung: {jarak_langsung:.2f} km")
    
    # Hitung detour tiap SPBU
    hasil = []
    print("\n[PERHITUNGAN DETOUR]")
    for spbu in spbu_list:
        jarak_total = hitung_jarak(driver, spbu) + hitung_jarak(spbu, customer)
        detour = jarak_total - jarak_langsung
        hasil.append({"spbu": spbu, "jarak": jarak_total, "detour": detour})
        print(f"  {spbu['nama']}: jarak={jarak_total:.2f} km, detour=+{detour:.2f} km")
    
    # Pilih detour terkecil (Greedy)
    hasil.sort(key=lambda x: x['detour'])
    terpilih = hasil[0]
    
    print(f"\n[HASIL] SPBU Terpilih: {terpilih['spbu']['nama']}")
    print(f"  Detour: +{terpilih['detour']:.2f} km")


# ============================================================
# FITUR B.1: BACKTRACKING - GENERATE RUTE
# ============================================================
def fitur_b1_rute():
    """Generate semua rute valid dengan backtracking"""
    print("\n" + "=" * 60)
    print("FITUR B.1: GENERATE SEMUA RUTE VALID")
    print("Algoritma: Backtracking")
    print("=" * 60)
    
    database = CONTOH_CUSTOMERS
    batas_jarak = BATAS_JARAK_MAKSIMAL
    target = len(database)
    
    print(f"\n[DATA INPUT]")
    for c in database:
        print(f"  {c['id']}: {c['nama']}, zona={c['zona']}, jarak={c['jarak']} km")
    print(f"  Batas jarak: {batas_jarak} km")
    
    def is_aman(posisi, target_customer):
        total_jarak = sum(c['jarak'] for c in posisi)
        if total_jarak + target_customer['jarak'] > batas_jarak:
            return False
        if len(posisi) >= 2:
            if target_customer['zona'] == posisi[-1]['zona'] == posisi[-2]['zona']:
                return False
        return True
    
    def backtrack(posisi, index_used, hasil):
        if len(posisi) == target:
            zona_unik = set(c['zona'] for c in posisi)
            if len(zona_unik) >= 2:
                hasil.append(list(posisi))
            return
        
        for i in range(len(database)):
            if i not in index_used and is_aman(posisi, database[i]):
                posisi.append(database[i])
                index_used.add(i)
                backtrack(posisi, index_used, hasil)
                posisi.pop()
                index_used.remove(i)
    
    solusi = []
    backtrack([], set(), solusi)
    
    print(f"\n[HASIL] Ditemukan {len(solusi)} rute valid:")
    for i, rute in enumerate(solusi[:5], 1):  # Tampilkan max 5
        nama = [c['nama'] for c in rute]
        zona = [c['zona'] for c in rute]
        total = sum(c['jarak'] for c in rute)
        print(f"  {i}. {nama} | zona: {zona} | {total} km")
    
    if len(solusi) > 5:
        print(f"  ... dan {len(solusi)-5} rute lainnya")


# ============================================================
# FITUR B.2: BACKTRACKING - KOMBINASI PROMO
# ============================================================
def fitur_b2_promo():
    """Generate kombinasi promo valid dengan backtracking"""
    print("\n" + "=" * 60)
    print("FITUR B.2: KOMBINASI PROMO VALID")
    print("Algoritma: Backtracking")
    print("=" * 60)
    
    promo_list = CONTOH_PROMO
    keranjang = CONTOH_KERANJANG
    
    print(f"\n[DATA KERANJANG]")
    print(f"  Total: Rp{keranjang['total']:,}")
    print(f"  Kategori: {keranjang['kategori']}")
    print(f"  Hari: {keranjang['hari']}, Status: {keranjang['status_user']}")
    
    batas_diskon = keranjang['total'] * 0.5
    
    def cek_berlaku(promo):
        if promo['kategori'] != 'semua' and promo['kategori'] not in keranjang['kategori']:
            return False
        if keranjang['total'] < promo['min_pembelian']:
            return False
        if promo['syarat'] != 'semua':
            if promo['syarat'] == 'weekend' and keranjang['hari'] != 'weekend':
                return False
            if promo['syarat'] == 'new_user' and keranjang['status_user'] != 'new_user':
                return False
            if promo['syarat'] == 'member' and keranjang['status_user'] != 'member':
                return False
        return True
    
    promo_valid = [p for p in promo_list if cek_berlaku(p)]
    
    print(f"\n[PROMO APPLICABLE]")
    for p in promo_valid:
        print(f"  {p['id']}: {p['nama']} (Rp{p['diskon']:,})")
    
    hasil = []
    
    def backtrack(index, kombinasi, total_diskon):
        if len(kombinasi) > 0 and total_diskon <= batas_diskon:
            hasil.append({
                "promo": [p['nama'] for p in kombinasi],
                "diskon": total_diskon
            })
        if len(kombinasi) >= 2:
            return
        for i in range(index, len(promo_valid)):
            p = promo_valid[i]
            if total_diskon + p['diskon'] <= batas_diskon:
                # Cek syarat tidak bentrok
                bentrok = False
                if p['syarat'] != 'semua':
                    for existing in kombinasi:
                        if existing['syarat'] == p['syarat']:
                            bentrok = True
                if not bentrok:
                    kombinasi.append(p)
                    backtrack(i+1, kombinasi, total_diskon + p['diskon'])
                    kombinasi.pop()
    
    backtrack(0, [], 0)
    
    print(f"\n[HASIL] Ditemukan {len(hasil)} kombinasi valid:")
    for i, h in enumerate(hasil, 1):
        print(f"  {i}. {' + '.join(h['promo'])} = Rp{h['diskon']:,}")


# ============================================================
# FITUR C.1: DYNAMIC PROGRAMMING - KNAPSACK
# ============================================================
def fitur_c1_knapsack():
    """Optimasi kapasitas tas dengan DP Knapsack"""
    print("\n" + "=" * 60)
    print("FITUR C.1: OPTIMASI KAPASITAS TAS")
    print("Algoritma: Dynamic Programming (0/1 Knapsack)")
    print("=" * 60)
    
    items = CONTOH_ITEMS_DELIVERY
    kapasitas = KAPASITAS_TAS
    
    print(f"\n[DATA INPUT]")
    for item in items:
        print(f"  {item['id']}: {item['nama']} | {item['volume']} cm3 | Rp{item['tip']:,}")
    print(f"  Kapasitas tas: {kapasitas:,} cm3")
    
    n = len(items)
    dp = [[0]*(kapasitas+1) for _ in range(n+1)]
    
    # Build DP table
    for i in range(1, n+1):
        vol = items[i-1]['volume']
        tip = items[i-1]['tip']
        for w in range(kapasitas+1):
            if vol <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-vol] + tip)
            else:
                dp[i][w] = dp[i-1][w]
    
    # Backtrack
    terpilih = []
    w = kapasitas
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            terpilih.append(items[i-1])
            w -= items[i-1]['volume']
    terpilih.reverse()
    
    total_vol = sum(item['volume'] for item in terpilih)
    total_tip = sum(item['tip'] for item in terpilih)
    
    print(f"\n[HASIL] Item terpilih:")
    for item in terpilih:
        print(f"  - {item['nama']} ({item['volume']} cm3, Rp{item['tip']:,})")
    print(f"\n  Total volume: {total_vol:,} cm3")
    print(f"  Total tip   : Rp{total_tip:,}")


# ============================================================
# FITUR C.2: DYNAMIC PROGRAMMING - COIN CHANGE
# ============================================================
def fitur_c2_topup():
    """Minimalisasi transaksi top-up dengan DP"""
    print("\n" + "=" * 60)
    print("FITUR C.2: MINIMALISASI TRANSAKSI TOP-UP")
    print("Algoritma: Dynamic Programming (Coin Change)")
    print("=" * 60)
    
    target = CONTOH_TARGET_SALDO
    nominal = CONTOH_NOMINAL_TOPUP
    
    print(f"\n[DATA INPUT]")
    print(f"  Target saldo: Rp{target:,}")
    print(f"  Nominal tersedia: {[f'Rp{n:,}' for n in nominal]}")
    
    # Sederhanakan (bagi 1000)
    factor = 1000
    target_s = target // factor
    nominal_s = [n // factor for n in nominal]
    
    INF = float('inf')
    dp = [INF] * (target_s + 1)
    choice = [-1] * (target_s + 1)
    dp[0] = 0
    
    for s in range(1, target_s + 1):
        for nom in nominal_s:
            if nom <= s and dp[s-nom] + 1 < dp[s]:
                dp[s] = dp[s-nom] + 1
                choice[s] = nom
    
    if dp[target_s] == INF:
        print("\n[HASIL] Tidak ada kombinasi yang tepat")
        return
    
    # Backtrack
    kombinasi = []
    s = target_s
    while s > 0:
        kombinasi.append(choice[s] * factor)
        s -= choice[s]
    
    print(f"\n[HASIL]")
    print(f"  Jumlah transaksi minimal: {dp[target_s]}")
    print(f"  Kombinasi: {[f'Rp{n:,}' for n in kombinasi]}")
    print(f"  Total: Rp{sum(kombinasi):,}")


# ============================================================
# MENU UTAMA
# ============================================================
def tampilkan_menu():
    print("\n" + "=" * 60)
    print("        SISTEM DELIVERY MAKANCEPAT")
    print("        Final Project - Algorithm Foundations")
    print("=" * 60)
    print("\n[GREEDY ALGORITHM]")
    print("  1. Fitur A.1 - Penjadwalan Time Window (EDF)")
    print("  2. Fitur A.2 - Urutan Masak Optimal (SPT)")
    print("  3. Fitur A.3 - Pengisian Bensin Efisien (Min Detour)")
    print("\n[BACKTRACKING]")
    print("  4. Fitur B.1 - Generate Semua Rute Valid")
    print("  5. Fitur B.2 - Kombinasi Promo Valid")
    print("\n[DYNAMIC PROGRAMMING]")
    print("  6. Fitur C.1 - Optimasi Kapasitas Tas (Knapsack)")
    print("  7. Fitur C.2 - Minimum Transaksi Top-up (Coin Change)")
    print("\n[LAINNYA]")
    print("  8. Jalankan Semua Fitur")
    print("  0. Keluar")
    print("-" * 60)


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih fitur (0-8): ").strip()
        
        if pilihan == "1":
            fitur_a1_timewindow()
        elif pilihan == "2":
            fitur_a2_masak()
        elif pilihan == "3":
            fitur_a3_spbu()
        elif pilihan == "4":
            fitur_b1_rute()
        elif pilihan == "5":
            fitur_b2_promo()
        elif pilihan == "6":
            fitur_c1_knapsack()
        elif pilihan == "7":
            fitur_c2_topup()
        elif pilihan == "8":
            fitur_a1_timewindow()
            fitur_a2_masak()
            fitur_a3_spbu()
            fitur_b1_rute()
            fitur_b2_promo()
            fitur_c1_knapsack()
            fitur_c2_topup()
        elif pilihan == "0":
            print("\nTerima kasih! Sampai jumpa.\n")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
        
        input("\nTekan Enter untuk melanjutkan...")


if __name__ == "__main__":
    main()
