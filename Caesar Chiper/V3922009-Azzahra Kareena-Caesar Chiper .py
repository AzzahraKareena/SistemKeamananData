#!/usr/bin/env python
# coding: utf-8

# In[2]:


def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Mengecek apakah karakter adalah huruf
            if char.islower():  # Mengecek apakah huruf adalah huruf kecil
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
                # Mengenkripsi huruf kecil dengan menggeser karakter sesuai dengan kunci pergeseran
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
                # Mengenkripsi huruf besar dengan menggeser karakter sesuai dengan kunci pergeseran
        else:
            encrypted_char = char  # Karakter non-alfabet tidak diubah
        encrypted_text += encrypted_char
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():  # Mengecek apakah karakter adalah huruf
            if char.islower():  # Mengecek apakah huruf adalah huruf kecil
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
                # Mendekripsi huruf kecil dengan menggeser karakter sesuai dengan kunci pergeseran
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
                # Mendekripsi huruf besar dengan menggeser karakter sesuai dengan kunci pergeseran
        else:
            decrypted_char = char  # Karakter non-alfabet tidak diubah
        decrypted_text += decrypted_char
    return decrypted_text

# Input teks dan kunci pergeseran
plaintext = "Have Fun Studying Cryptography"  # Teks yang akan dienkripsi
shift = 8  # Kunci pergeseran

# Enkripsi teks
encrypted_text = caesar_encrypt(plaintext, shift)
print("Plaintext: ", plaintext)
print("Ciphertext:", encrypted_text)

# Dekripsi teks
decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Decrypted Text:", decrypted_text)


# In[ ]:




