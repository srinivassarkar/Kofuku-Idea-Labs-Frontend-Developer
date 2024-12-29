## Input


```json
{
  "decrypted_text": "CONGRATULATIONSYOUCOMPLETEDTHEASSIGNMENT",
  "email": "srinivassarkar07@gmail.com",
  "phone_number": "9346179776",
  "name": "Srinivas Sarkar",
  "user_submitted_code": "def decrypt_vigenere(ciphertext, key):\n    plaintext = \"\"\n    key_length = len(key)\n    for i, c in enumerate(ciphertext):\n        if c.isalpha():\n            key_char = key[i % key_length]\n            shift = ord(key_char.upper()) - ord('A')\n            if c.islower():\n                plaintext += chr((ord(c) - ord('a') - shift + 26) % 26 + ord('a'))\n            else:\n                plaintext += chr((ord(c) - ord('A') - shift + 26) % 26 + ord('A'))\n        else:\n            plaintext += c\n    return plaintext\n\n# The encrypted text and key received\nencrypted_text = \"RXDLQCRDUHUOUEVLPYQEXABGUWABFUUIIDURHCVZ\"\nkey = \"PJQFZCYJJHBGGRDNBEOQLLQCBSXIYQUQQVOEVYIG\"\n\n# Decrypted message\ndecrypted_text = decrypt_vigenere(encrypted_text, key)\nprint(\"Decrypted Text:\", decrypted_text)"
}
