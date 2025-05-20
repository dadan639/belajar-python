
data_suhu = [
    [25, 26, 27, 24, 25, 28, 29],  # Minggu 1
    [30, 31, 29, 28, 30, 32, 33],  # Minggu 2
    [23, 24, 25, 22, 23, 26, 27],  # Minggu 3
    [28, 29, 30, 27, 28, 31, 32],  # Minggu 4
    [26, 27, 28, 25, 26, 29, 30]   # Minggu 5
]

for i in range(len(data_suhu)):
    minggu = data_suhu[i]
    total_suhu = 0
    hari_ke = 0
    while hari_ke < len(minggu):
        total_suhu += minggu[hari_ke]
        hari_ke += 1
    rata_rata = total_suhu / len(minggu)
    print(f"Rata-rata suhu Minggu ke-{i+1}: {rata_rata:.2f} Celsius")

print("....")

suhu_tertinggi = -float('inf')
minggu_tertinggi = 0
hari_tertinggi = 0

for i in range(len(data_suhu)):
    for j in range(len(data_suhu[i])):
        if data_suhu[i][j] > suhu_tertinggi:
            suhu_tertinggi = data_suhu[i][j]
            minggu_tertinggi = i + 1
            hari_tertinggi = j + 1

print(f"Suhu tertinggi adalah {suhu_tertinggi} Celsius, terjadi pada hari ke-{hari_tertinggi} di Minggu ke-{minggu_tertinggi}")

print("....")

kenaikan_terbesar = -1
minggu_kenaikan_terbesar = 0

for i in range(1, len(data_suhu)):
    minggu_sekarang = data_suhu[i]
    minggu_sebelumnya = data_suhu[i-1]
    total_kenaikan = 0
    for j in range(len(minggu_sekarang)):
        selisih = minggu_sekarang[j] - minggu_sebelumnya[j]
        if selisih > 0:
            total_kenaikan += selisih
    if total_kenaikan > kenaikan_terbesar:
        kenaikan_terbesar = total_kenaikan
        minggu_kenaikan_terbesar = i + 1

print(f"Minggu dengan kenaikan suhu terbesar adalah: Minggu ke-{minggu_kenaikan_terbesar}")
print("....")