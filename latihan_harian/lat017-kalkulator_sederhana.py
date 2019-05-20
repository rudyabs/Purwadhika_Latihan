# KALKULATOR SEDERHANA
    # Input angka pertama
    # Input operator
    # Input angka kedua
    # output = hasil

# KONVERSI MATA UANG (IDR => USD / USD => IDR)
    # INPUT KONVERSI YG DIINGINKAN
    # INPUT NILAI NOMINAL MATA UANG
    # HASIL KONVERSI

# PENGHITUNG BMI (BODY MASS INDEX)
    # RUMUS ADA DI INTERNET

# def add(x, y):
#     return x + y

# def substract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     return x / y

print('''Masuk operasi yang diinginkan?
+ untuk tambah
- untuk kurang
* untuk kali
/ untuk bagi
''')

# Memasukan input user

pilihan = input("Pilihlah operasi matematika yang diinginkan: ")

x = int(input("Masukan angka pertama: "))

y = int(input("Masukan angka kedua: "))

if pilihan == '+':
    print("{} + {} = ".format(x, y))
    print(x + y)
elif pilihan == '-':
    print("{} - {} = ".format(x, y))
    print(x - y)
elif pilihan == '*':
    print("{} * {} = ".format(x, y))
    print(x * y)
elif pilihan == '/':
    print("{} / {} = ".format(x, y))
    print(x / y)
else:
    print("Input yang anda masukan salah!")
    




