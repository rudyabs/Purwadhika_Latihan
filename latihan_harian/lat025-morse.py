# buat program translate morse dan kebalikannya
code_morse = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

code_morse_reversed = {value:key for key,value in code_morse.items()}



def to_morse(user_input):
    return ' '.join(code_morse.get(i.upper()) for i in user_input)

def from_morse(user_input):
    return ''.join(code_morse_reversed.get(i) for i in user_input.split())

pilihan_translate = input('''Masukan operasi yang diinginkan:
1. Ubah alphabet ke morse
2. Ubah morse ke alphabet
''')
user_input = input('Masukan kata yang ingin diubah: ' )

if pilihan_translate == '1':
    print(to_morse(user_input))
elif pilihan_translate == '2':
    print(from_morse(user_input))
else:
    print('Operasi atau kata yang anda masukan salah!')
