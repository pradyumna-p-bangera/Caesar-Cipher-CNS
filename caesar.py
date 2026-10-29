def caesar_encrypt(plaintext, shift):
    """Encrypts plaintext using Caesar Cipher with a given shift."""
    ciphertext = ""
    for char in plaintext:
        if char.isupper():
            # Shift uppercase characters
            ciphertext += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            # Shift lowercase characters
            ciphertext += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Leave spaces, numbers, and punctuation unchanged
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    """Decrypts ciphertext using Caesar Cipher with a given shift."""
    plaintext = ""
    for char in ciphertext:
        if char.isupper():
            plaintext += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            plaintext += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plaintext += char
    return plaintext

# --- Comprehensive Test Cases ---
if __name__ == "__main__":
    print("=== Caesar Cipher Test Execution ===")
    
    test_message = "Cryptography and Network Security Assignment!"
    shift_key = 4
    
    encrypted_msg = caesar_encrypt(test_message, shift_key)
    decrypted_msg = caesar_decrypt(encrypted_msg, shift_key)
    
    print(f"Original Text : {test_message}")
    print(f"Shift Key     : {shift_key}")
    print(f"Encrypted Text: {encrypted_msg}")
    print(f"Decrypted Text: {decrypted_msg}")