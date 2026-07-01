#build a Caesar cipher. 
# This is one of the simplest techniques to encrypt text,
# which consists of substituting each letter of the plain text 
# with the letter found at a fixed number of positions down the alphabet. 
# For example, with a shift of 5, a would be replaced by f, b by g and so on.


'''
Create a program called caesar cipher which is
an encryption method that shifts letters in the alphabet to encode messages.
'''


def caesar(text, shift, encrypt=True):
# Validasi 1: Memastikan nilai pergeseran (shift) harus berupa angka bulat
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
# Validasi 2: Memastikan nilai pergeseran berada di rentang alfabet yang valid (1-25)
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'
# Representasi alfabet standar sebagai acuan karakter
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    # Membuat susunan alfabet baru yang sudah tergeser menggunakan teknik slicing
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    
    # Membuat kamus pemetaan karakter (maketrans) untuk huruf kecil dan huruf kapital
    translation_table = str.maketrans(alphabet + alphabet.upper(),
                        shifted_alphabet + shifted_alphabet.upper())
    
    # Menerjemahkan teks asli ke teks tersandi
    encrypted_text = text.translate(translation_table)
    return encrypted_text

# Fungsi perantara khusus untuk mengunci pesan (Enkripsi)
def encrypt(text, shift):
    return caesar(text, shift)
# Fungsi perantara khusus untuk membuka pesan tersandi (Dekripsi)    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

# #Testing the Caesar cipher functions
# encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
# print(encrypted_text)

# decrypted_text=decrypt(encrypted_text, 13)
# print('Hasil decode:', decrypted_text)

print('========== Aplikasi Caesar Cipher ==========')
print('1. Encrypt a message')
print('2. Decrypt a message')

pilihan=int(input('Masukan pilihan anda (1/2): '))
user_text=input('Masukan teks: ')
user_shift=int(input('Masukan nilai pergeseran (1-25): '))

if pilihan==1:
    hasil_encrypt=encrypt(user_text, user_shift)
    print('Hasil enkripsi:', hasil_encrypt)
elif pilihan ==2:
    hasil_decrypt=decrypt(user_text, user_shift)
    print('Hasil dekripsi:', hasil_decrypt)
else:
    print('Pilihan tidak valid. Silakan pilih 1 atau 2.')