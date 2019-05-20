# kurs mata uang
kurs = {
    '1': 0.00071,
    '2': 14157
}

def konversi():
    print('''Selamat datang di web KonversiDuit.com
    Silahkan pilih metode konversi:
    1. IDR ke USD
    2. USD ke IDR
    ''')
    metode = input('Ketik pilihan metode yang digunakan: ')
    if metode == '1':
        nominal = input('Ketik nominal Rupiah yang diinginkan: Rp ')
        if nominal.replace('.', '').replace(',', '').isdigit():
            hasil = float(nominal.replace(',', '.')) * kurs[metode]
            print('Konversi Rp', nominal, '= $', hasil)
        else:
            print("Hanya menerima input angka!")
    elif metode == '2':
        nominal = input('Ketik nominal Dollar yang diinginkan: $ ')
        if nominal.replace('.', '').replace('.', '').isdigit():
            hasil = float(nominal.replace(',', '.')) * kurs[metode]
            print(nominal)
            print('Konversi $', nominal, '= Rp', hasil)
        else:
            print("Hanya menerima input angka!")
    else:
        print('Pilihan yang tersedia hanya 1 dan 2, silahkan coba kembali.')
konversi()