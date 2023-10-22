#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Fungsi untuk melakukan enkripsi teks dengan sandi Caesar
def caesar_cipher(text, shift_key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()  # Menyimpan informasi apakah karakter asli adalah huruf besar
            char = char.upper()  # Mengubah karakter menjadi huruf besar untuk pencocokan dengan shift_key
            if char in shift_key:
                shifted_char = shift_key[char]  # Mengambil karakter terenkripsi dari shift_key
                if not is_upper:
                    shifted_char = shifted_char.lower()  # Mengembalikan huruf ke huruf kecil jika karakter asli adalah huruf kecil
                encrypted_text += shifted_char
            else:
                encrypted_text += char  # Menambahkan karakter asli jika tidak ditemukan dalam shift_key
        else:
            encrypted_text += char  # Menambahkan karakter asli jika bukan huruf
    return encrypted_text

# Teks yang akan dienkripsi
plaintext = "Success is not final, failure is not fatal, it is the courage to continue that counts."

# Kunci enkripsi (pemetaan huruf asli ke huruf terenkripsi)
shift_key = {
    'A': 'R',
    'B': 'E',
    'C': 'N',
    'D': 'A',
    'E': 'B',
    'F': 'C',
    'G': 'D',
    'H': 'F',
    'I': 'G',
    'J': 'H',
    'K': 'I',
    'L': 'J',
    'M': 'K',
    'N': 'L',
    'O': 'M',
    'P': 'O',
    'Q': 'P',
    'R': 'Q',
    'S': 'S',
    'T': 'T',
    'U': 'U',
    'V': 'V',
    'W': 'W',
    'X': 'X',
    'Y': 'Y',
    'Z': 'Z'
}

# Fungsi untuk melakukan dekripsi teks yang telah dienkripsi dengan sandi Caesar
def caesar_decipher(encrypted_text, shift_key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            is_upper = char.isupper()  # Menyimpan informasi apakah karakter terenkripsi adalah huruf besar
            char = char.upper()  # Mengubah karakter terenkripsi menjadi huruf besar untuk pencocokan dengan shift_key.values()
            if char in shift_key.values():
                original_char = [k for k, v in shift_key.items() if v == char][0]  # Mendekripsi karakter dengan mencari pasangan di shift_key
                if not is_upper:
                    original_char = original_char.lower()  # Mengembalikan huruf ke huruf kecil jika karakter terenkripsi adalah huruf kecil
                decrypted_text += original_char
            else:
                decrypted_text += char  # Menambahkan karakter terenkripsi jika tidak ditemukan dalam shift_key.values()
        else:
            decrypted_text += char  # Menambahkan karakter non-alfabet tanpa perubahan
    return decrypted_text

# Enkripsi teks
encrypted_text = caesar_cipher(plaintext, shift_key)
print(f'Hasil Enkripsi : {encrypted_text}')

# Dekripsi teks yang telah dienkripsi
decrypted_text = caesar_decipher(encrypted_text, shift_key)
print(f'Hasil Dekripsi : {decrypted_text}')


# In[11]:


# Fungsi untuk memberi padding kunci Vigenere dengan teks asli
def _pad_key(plaintext, key):
    padded_key = ''
    i = 0
    for char in plaintext:
        if char.isalpha():
            padded_key += key[i % len(key)]  # Gunakan kunci secara berulang
            i += 1
        else:
            padded_key += ' '  # Tambahkan spasi jika karakter bukan huruf
    return padded_key

# Fungsi untuk mengenkripsi satu karakter dengan Vigenere Cipher
def _encrypt_char(plaintext_char, key_char):
    if plaintext_char.isalpha():
        first_alphabet_letter = 'a'
        if plaintext_char.isupper():
            first_alphabet_letter = 'A'

        old_char_position = ord(plaintext_char) - ord(first_alphabet_letter)
        key_char_position = ord(key_char.lower()) - ord('a')

        new_char_position = (old_char_position + key_char_position) % 26 + 1  # Mengenkripsi karakter
        return chr(new_char_position + ord(first_alphabet_letter))

    return plaintext_char

# Fungsi untuk mendekripsi satu karakter dengan Vigenere Cipher
def _decrypt_char(ciphertext_char, key_char):
    if ciphertext_char.isalpha():
        first_alphabet_letter = 'a'
        if ciphertext_char.isupper():
            first_alphabet_letter = 'A'

        old_char_position = ord(ciphertext_char) - ord(first_alphabet_letter)
        key_char_position = ord(key_char.lower()) - ord('a')

        new_char_position = (old_char_position - key_char_position) % 26-1  # Mendekripsi karakter
        return chr(new_char_position + ord(first_alphabet_letter))

    return ciphertext_char

# Fungsi untuk mengenkripsi teks dengan Vigenere Cipher
def encrypt(plaintext, key):
    ciphertext = ''
    padded_key = _pad_key(plaintext, key)
    for plaintext_char, key_char in zip(plaintext, padded_key):
        ciphertext += _encrypt_char(plaintext_char, key_char)
    return ciphertext

# Fungsi untuk mendekripsi teks yang telah dienkripsi dengan Vigenere Cipher
def decrypt(ciphertext, key):
    plaintext = ''
    padded_key = _pad_key(ciphertext, key)
    for ciphertext_char, key_char in zip(ciphertext, padded_key):
        if ciphertext_char.isalpha():
            plaintext += _decrypt_char(ciphertext_char, key_char)
        else:
            plaintext += ciphertext_char  # Tambahkan karakter non-alphabetic langsung ke plaintext
    return plaintext

# Meminta pengguna untuk memasukkan teks dan kunci
plaintext = input('Plaintext: ')
key = input('Kunci: ')

# Melakukan enkripsi dengan Vigenere Cipher
ciphertext = encrypt(plaintext, key)

# Melakukan dekripsi teks yang telah dienkripsi
decrypted_plaintext = decrypt(ciphertext, key)

# Menampilkan hasil enkripsi dan dekripsi
print(f'Ciphertext: {ciphertext.replace("{", " ")}')  # Mengganti karakter '{' dengan spasi untuk kejelasan
print(f'Decrypted Plaintext: {decrypted_plaintext.replace("{", " ")}')


# In[ ]:




