# ============================================================
# Program 3: AES Algorithm
# Required Packages: pycryptodome
# Install: pip install pycryptodome
# ============================================================

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from secrets import token_bytes


# ---------------- Main ----------------
print("--- AES Algorithm ---")
text = input("Enter text to encrypt: ")

key = token_bytes(16)   # AES-128 requires 16-byte key

cipher = AES.new(key, AES.MODE_CBC)
iv = cipher.iv
encrypted = cipher.encrypt(pad(text.encode('utf-8'), AES.block_size))

decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(decipher.decrypt(encrypted), AES.block_size).decode('utf-8')

print("Key (hex)      :", key.hex())
print("IV  (hex)      :", iv.hex())
print("Encrypted (hex):", encrypted.hex())
print("Decrypted Text :", decrypted)
