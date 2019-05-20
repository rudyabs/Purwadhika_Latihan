# Password

# variable id dan pass
username = 'baba'
sandi = '123456'
count = 0

# loop
while True:
    username = input("Masukan username anda: ")
    sandi = input("Masukukan password anda: ")
    count += 1
    # Jika kesalahan sudah mencapai 3 kali
    if count == 3:
        print("Kesalahan anda mencapai 3 kali")
        break
    else:
        #  Jika ID/Pass yang dimasukan benar
        if username == 'baba' and sandi =='123456':
            print("Welcome", username)
            break
        else:
            # Jika ID/Pass yang dimasukan salah.
            print("""Maaf username atau password yang anda masukan salah!
            Silahkan masukan kembali username dan password anda.
            """)
            continue



    
    