#!/usr/bin/env python
# coding: utf-8

# In[2]:


def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_len = len(key)
    
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():  # Mengecek apakah karakter adalah huruf
            shift = ord(key[i % key_len]) - ord('A')  # Menggunakan kunci untuk menentukan pergeseran
            if char.islower():  # Mengecek apakah huruf adalah huruf kecil
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
                # Mengenkripsi huruf kecil dengan Vigenere Cipher
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
                # Mengenkripsi huruf besar dengan Vigenere Cipher
        else:
            encrypted_char = char  # Karakter non-alfabet tidak diubah
        encrypted_text += encrypted_char
    
    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_len = len(key)
    
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():  # Mengecek apakah karakter adalah huruf
            shift = ord(key[i % key_len]) - ord('A')  # Menggunakan kunci untuk menentukan pergeseran
            if char.islower():  # Mengecek apakah huruf adalah huruf kecil
                decrypted_char = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
                # Mendekripsi huruf kecil dengan Vigenere Cipher
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
                # Mendekripsi huruf besar dengan Vigenere Cipher
        else:
            decrypted_char = char  # Karakter non-alfabet tidak diubah
        decrypted_text += decrypted_char
    
    return decrypted_text

# Input teks dan kunci (kota tempat tinggal)
plain_text = "Azzahra Kareena Rendriputri"  # Teks yang akan dienkripsi
key = "Madiun"  # Kunci (kota tempat tinggal)

# Enkripsi teks
encrypted_text = vigenere_encrypt(plain_text, key)
print("Plaintext: ", plain_text)
print("Ciphertext:", encrypted_text)

# Dekripsi teks
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)


# In[ ]:




