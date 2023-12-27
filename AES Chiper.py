#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Impor modul yang diperlukan dari pustaka Crypto
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

# Menghasilkan salt (garam) acak dengan panjang 16 byte
salt = get_random_bytes(16)

# Menghasilkan kunci turunan dari passphrase menggunakan PBKDF2
passphrase = "Silaturahmi"
key = PBKDF2(passphrase, salt, dkLen=32, count=1000000)  # Ganti dkLen sesuai dengan panjang yang Anda inginkan

# Membuat instansi cipher AES baru dalam mode EAX
cipher = AES.new(key, AES.MODE_EAX)

# Data yang akan dienkripsi
data = "Kelompok Enam".encode()

# Nonce adalah nilai acak yang digenerate setiap kali kita membuat instansi cipher menggunakan new()
nonce = cipher.nonce

# Melakukan enkripsi terhadap data
ciphertext = cipher.encrypt(data)

# Menampilkan data yang telah dienkripsi
print("Cipher text:", ciphertext)

# Membuat instansi baru dengan kunci dan nonce yang sama seperti instansi enkripsi
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

# Melakukan dekripsi terhadap data
plaintext = cipher.decrypt(ciphertext)
print("Plain text:", plaintext.decode())


# In[ ]:




