def decrypt_vigenere(ciphertext, key):
    plaintext = ""
    key_length = len(key)
    for i, c in enumerate(ciphertext):
        if c.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.upper()) - ord('A')
            if c.islower():
                plaintext += chr((ord(c) - ord('a') - shift + 26) % 26 + ord('a'))
            else:
                plaintext += chr((ord(c) - ord('A') - shift + 26) % 26 + ord('A'))
        else:
            plaintext += c
    return plaintext

# The encrypted text and key i.e received
encrypted_text = "RXDLQCRDUHUOUEVLPYQEXABGUWABFUUIIDURHCVZ"
key = "PJQFZCYJJHBGGRDNBEOQLLQCBSXIYQUQQVOEVYIG"

# Decrypted message
decrypted_text = decrypt_vigenere(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
