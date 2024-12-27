# TASK-1 PYTHON PROGRAMMING.

#1. custom Encryption - Decreption System

# Caesar Cipher Encryption
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
           
            start = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - start + shift) % 26 + start)
        else:
           
            encrypted_text += char
    return encrypted_text

# Caesar Cipher Decryption
def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
          
            start = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - start - shift) % 26 + start)
        else:
          
            decrypted_text += char
    return decrypted_text


message = input("Enter a message to encrypt: ")
shift = int(input("Enter shift value (integer): "))

encrypted_message = encrypt(message, shift)
print(f"Encrypted message: {encrypted_message}")

decrypted_message = decrypt(encrypted_message, shift)
print(f"Decrypted message: {decrypted_message}")
