data_penjualan = [
    {'nama_produk': 'Laptop A', 'penjualan_harian': [10, 12, 15, 11, 13, 16, 14]},
    {'nama_produk': 'Mouse B', 'penjualan_harian': [25, 28, 30, 27, 29, 32, 31]},
    {'nama_produk': 'Keyboard C', 'penjualan_harian': [8, 9, 10, 7, 8, 11, 10]},
    {'nama_produk': 'Monitor D', 'penjualan_harian': [5, 6, 7, 5, 6, 8, 7]},
]

#total penjualan mingguan per produk
print("--- Total Penjualan Mingguan per Produk ---")
for produk in data_penjualan:
    nama_produk = produk['nama_produk']
    penjualan_harian = produk['penjualan_harian']
    total_penjualan = 0
    hari_ke = 0
    while hari_ke < len(penjualan_harian):
        total_penjualan += penjualan_harian[hari_ke]
        hari_ke += 1
    print(f"Total penjualan {nama_produk}: {total_penjualan} unit")

#rata-rata penjualan harian semua produk
print("\n--- Rata-rata Penjualan Harian Semua Produk ---")
total_semua_penjualan = 0
total_hari_penjualan = 0
for produk in data_penjualan:
    for penjualan in produk['penjualan_harian']:
        total_semua_penjualan += penjualan
        total_hari_penjualan += 1

if total_hari_penjualan > 0:
    rata_rata_penjualan = total_semua_penjualan / total_hari_penjualan
    print(f"Rata - rata penjualan harian semua produk : {rata_rata_penjualan:.2f} unit")
else:
    print("Tidak ada data penjualan")

#produk dengan penjualan tertinggi di hari tertentu
print("\n--- Produk dengan penjualan tertinggi di hari tertentu ---")
while True:
    try:
        hari_input = int(input("Masukan nomor hari (1-7): "))
        if 1 <= hari_input <=7:
            break
        else:
            print("Nomor hari harus antara 1 dan 7")
    except ValueError:
        print("Input tidak valid, Masukan angka antara 1 dan 7")

hari_index = hari_input - 1
penjualan_tertinggi_hari_itu = -1
produk_terlalis_hari_itu = []

for produk in data_penjualan:
    nama_produk = produk['nama_produk']
    penjualan_harian_ini = produk['penjualan_harian'][hari_index]
    if penjualan_harian_ini > penjualan_tertinggi_hari_itu:
        penjualan_tertinggi_hari_itu = penjualan_harian_ini
        produk_terlalis_hari_itu =  [nama_produk]
    elif penjualan_harian_ini == penjualan_tertinggi_hari_itu:
        produk_terlalis_hari_itu.append(nama_produk)

if produk_terlalis_hari_itu:
    print(f"Produk dengan penjualan tertinggi di hari ke-{hari_input}: {', '.join(produk_terlalis_hari_itu)}")    
else:
    print(f"Tidak ada penjualan di hari ke-{hari_input}")   
