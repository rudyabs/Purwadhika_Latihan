# Buat file baru dengan 
list = ['Andi', 'Budi', 'Coco', 'Dano']

file = open('contoh2.txt', 'a')

for x in list:
    file.write('\n' + x)