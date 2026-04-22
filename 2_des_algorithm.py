# ============================================================
# Program 2: DES Algorithm
# Required Packages: pycryptodome
# Install: pip install pycryptodome
# ============================================================

from Crypto.Cipher import DES
from secrets import token_bytes


def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text


# ---------------- Main ----------------
print("--- DES Algorithm ---")
text = input("Enter text to encrypt: ")

key = token_bytes(8)   # DES requires 8-byte key

cipher = DES.new(key, DES.MODE_ECB)
encrypted = cipher.encrypt(pad(text).encode('utf-8'))

decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(encrypted).decode('utf-8').rstrip()

print("Key (hex)      :", key.hex())
print("Encrypted (hex):", encrypted.hex())
print("Decrypted Text :", decrypted)
