# ============================================================
# Program 1a: Caesar Cipher
# Required Packages: None (uses built-in Python only)
# ============================================================

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decrypt(cipher, shift):
    return encrypt(cipher, -shift)


# ---------------- Main ----------------
print("--- Caesar Cipher ---")
text = input("Enter text: ")
shift = int(input("Enter shift value: "))

encrypted = encrypt(text, shift)
decrypted = decrypt(encrypted, shift)

print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)
