
def is_aman(posisi_sementara, target_customer,batas_jarak):
   # cek batas jarak
    total_jarak_saat_ini = sum(c['jarak'] for c in posisi_sementara)
    if total_jarak_saat_ini  + target_customer['jarak'] > batas_jarak:
        return False

    # validasi kesamaan zona
    if len(posisi_sementara) >= 2 :
        posisi_terakhir = posisi_sementara[-1]
        posisi_sebelum_terakhir = posisi_sementara[-2]
        if target_customer['zona'] == posisi_terakhir['zona'] == posisi_sebelum_terakhir['zona']:
            return False
    return True



def cek_rute(database, posisi_sementara, index_sementara, hasil, target_customer, batas_jarak):
    # base case
    if len(posisi_sementara) == target_customer:
        zona_unik = set(c['zona'] for c in posisi_sementara)
        if len(zona_unik) >= 2:
            hasil.append(list(posisi_sementara))
    

    # rekursif
    for i in range(len(database)):
        customer = database[i]
        if i not in index_sementara: 
            if is_aman(posisi_sementara,customer,batas_jarak):
                posisi_sementara.append(database[i])
                index_sementara.add(i)
                cek_rute(database, posisi_sementara, index_sementara, hasil, target_customer, batas_jarak)
                posisi_sementara.pop()
                index_sementara.remove(i)

    

database= [
    {'id':'C1','nama':'Budi','zona': 'A', 'jarak': 5},
    {'id':'C2','nama':'Ani','zona': 'B', 'jarak': 3},
    {'id':'C3','nama':'Citra','zona': 'A', 'jarak': 4},
    {'id':'C4','nama':'Dodi','zona': 'A', 'jarak': 6},
]
batas_jarak = 20
target_customer = 4

# penampung hasil
solusi_ditemukan = []


cek_rute(database, [], set(), solusi_ditemukan ,target_customer , batas_jarak)


for i, rute in enumerate(solusi_ditemukan, 1):
        urutan = [c['zona'] for c in rute]
        nama = [c['nama'] for c in rute]
        total_km = sum(c['jarak'] for c in rute)
        print(f"Rute {i}: nama {nama}  | zona {urutan} | Total: {total_km} km")
print(f'total semua kemungkinan rute adalah : {len(solusi_ditemukan)} rute')


