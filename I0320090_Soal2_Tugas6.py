#soal nomor 2 tugas 6

#menghitung nilai rata-rata
Data_nilai = int(input("Banyak data : "))
List_nilai = []
i = 1
while i <= Data_nilai:
    Nilai = int(input("Nilai Anda : "))
    List_nilai.append(Nilai)
    i = i + 1
Rata_rata = sum(List_nilai)/Data_nilai
print("Rata-rata rapot Anda adalah", Rata_rata)