#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np

# Matriks kunci enkripsi
key_matrix = np.array([[0, 25, 7],
                       [10, 17, 4],
                       [13, 15, 19]])

# Fungsi untuk mengubah teks menjadi matriks huruf (A=0, B=1, ..., Z=25)
def text_to_matrix(text):
    return [ord(char) - ord('A') for char in text]

# Fungsi untuk mengubah matriks huruf menjadi teks
def matrix_to_text(matrix):
    return ''.join([chr(char + ord('A')) for char in matrix])

# Fungsi untuk mengenkripsi teks menggunakan Hill Cipher
def hill_encrypt(plain_text, key_matrix):
    # Menghapus spasi dari teks dan mengubahnya menjadi huruf besar
    plain_text = plain_text.replace(" ", "").upper()
    plain_matrix = text_to_matrix(plain_text)
    key_size = key_matrix.shape[0]
    
    encrypted_matrix = []
    
    # Memeriksa apakah ukuran matriks teks dapat dibagi habis oleh ukuran matriks kunci
    if len(plain_matrix) % key_size != 0:
        raise ValueError("Ukuran matriks teks tidak sesuai dengan ukuran matriks kunci")
    
    # Iterasi melalui matriks huruf teks yang akan dienkripsi
    for i in range(0, len(plain_matrix), key_size):
        # Mengambil segmen matriks huruf dengan panjang sesuai dengan ukuran matriks kunci
        segment = np.array(plain_matrix[i:i+key_size])
        
        # Melakukan operasi dot product antara matriks kunci dan segmen matriks huruf, kemudian mengambil modulo 26
        encrypted_segment = np.dot(key_matrix, segment) % 26
        
        # Menambahkan hasil enkripsi segmen ke dalam matriks hasil enkripsi
        encrypted_matrix.extend(encrypted_segment)
    
    encrypted_text = matrix_to_text(encrypted_matrix)
    return encrypted_text

# Fungsi untuk mendekripsi teks menggunakan Hill Cipher
def hill_decrypt(encrypted_text, key_matrix):
    # Menghapus spasi dari teks dan mengubahnya menjadi huruf besar
    encrypted_text = encrypted_text.replace(" ", "").upper()
    encrypted_matrix = text_to_matrix(encrypted_text)
    
    # Menghitung matriks invers dari matriks kunci menggunakan numpy
    key_matrix_inverse = np.linalg.inv(key_matrix)
    
    # Memutar matriks invers dengan mengalikannya dengan determinan matriks kunci yang dibulatkan
    key_matrix_inverse = np.round(key_matrix_inverse * np.linalg.det(key_matrix))
    
    # Mengubah matriks invers menjadi tipe data integer dan mengambil modulo 26 untuk memastikan hasilnya tetap dalam rentang huruf alfabet
    key_matrix_inverse = key_matrix_inverse.astype(int) % 26
    
    # Inisialisasi matriks untuk teks terdekripsi
    decrypted_matrix = []
    
    # Mendapatkan ukuran matriks invers (seharusnya sama dengan ukuran matriks kunci)
    key_size = key_matrix_inverse.shape[0]
    
    # Iterasi melalui matriks huruf terenkripsi
    for i in range(0, len(encrypted_matrix), key_size):
        # Mengambil segmen matriks huruf sesuai dengan ukuran matriks invers
        segment = np.array(encrypted_matrix[i:i+key_size])
        
        # Mendekripsi segmen dengan melakukan operasi dot product dengan matriks invers dan mengambil modulo 26
        decrypted_segment = np.dot(key_matrix_inverse, segment) % 26
        
        # Menambahkan hasil dekripsi segmen ke dalam matriks hasil dekripsi
        decrypted_matrix.extend(decrypted_segment)
    
    # Mengubah matriks huruf terdekripsi menjadi teks
    decrypted_text = matrix_to_text(decrypted_matrix)
    
    # Mengembalikan teks terdekripsi
    return decrypted_text

# Input teks
plain_text = "Azzahra Kareenaa"

# Enkripsi teks
encrypted_text = hill_encrypt(plain_text, key_matrix)
print("Plaintext: ", plain_text)
print("Ciphertext:", encrypted_text)

# Dekripsi teks
decrypted_text = hill_decrypt(encrypted_text, key_matrix)
print("Decrypted Text:", decrypted_text)


# In[ ]:




