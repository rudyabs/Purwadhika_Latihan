nama = "rudy aunallah bumi satrio"

# Mengitung Jumlah Huruf Tanpa Spasi
'''
print(len(nama))
print(nama.split(" "))
print(len(nama.split(" ")))
'''

jumlah_spasi = len(nama.split(' ')) - 1
huruf_tanpa_spasi = len(nama) - jumlah_spasi
# print(jumlah_spasi)
print(f'Jumlah huruf tanpa spasi dari kata {nama} adalah {huruf_tanpa_spasi}')


# Menghitung Jumlah Huruf Tertentu "a"

# print(nama.split('a'))
# print(len(nama.split('a')))

jumlah_a = len(nama.split('a')) - 1
print(f'Jumlah huruf "a" dalam kata {nama} adalah {jumlah_a}')

# Menghitung spasi
# ada diatas
print(f'Jumlah spasi dalam kata {nama} adalah {jumlah_spasi}')