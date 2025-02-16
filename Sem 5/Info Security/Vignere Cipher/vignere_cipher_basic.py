def vigenere_encrypt(plaintext, key):
    # Convert the key to uppercase for uniformity in calculations
    key = key.upper()
    
    # List to hold the resulting encrypted text characters
    encrypted_text = []
    
    # Iterate through each character in the plaintext
    for i, char in enumerate(plaintext):
        # Only encrypt alphabetic characters, skip others (like spaces, punctuation)
        if char.isalpha():
            # Calculate the shift value by finding the corresponding letter in the key
            # The shift is determined by converting the key character to its position in the alphabet
            shift = ord(key[i % len(key)]) - ord('A')
            
            # Check if the character is uppercase
            if char.isupper():
                # Perform the Caesar cipher shift for uppercase letters
                # Convert the character to its position in the alphabet (0-25), apply the shift, and convert back to a character
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Perform the Caesar cipher shift for lowercase letters
                # Similar to the above, but for lowercase range (a-z)
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            
            # Append the encrypted character to the list
            encrypted_text.append(encrypted_char)
        else:
            # If the character is not alphabetic, keep it unchanged
            encrypted_text.append(char)
    
    # Join the list of characters into a single string and return the encrypted text
    return ''.join(encrypted_text)


def vigenere_decrypt(ciphertext, key):
    # Convert the key to uppercase for uniformity in calculations
    key = key.upper()
    
    # List to hold the resulting decrypted text characters
    decrypted_text = []
    
    # Iterate through each character in the ciphertext
    for i, char in enumerate(ciphertext):
        # Only decrypt alphabetic characters, skip others (like spaces, punctuation)
        if char.isalpha():
            # Calculate the shift value by finding the corresponding letter in the key
            # The shift is determined by converting the key character to its position in the alphabet
            shift = ord(key[i % len(key)]) - ord('A')
            
            # Check if the character is uppercase
            if char.isupper():
                # Perform the reverse Caesar cipher shift for uppercase letters
                # Convert the character to its position in the alphabet (0-25), subtract the shift, and convert back to a character
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                # Perform the reverse Caesar cipher shift for lowercase letters
                # Similar to the above, but for lowercase range (a-z)
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            
            # Append the decrypted character to the list
            decrypted_text.append(decrypted_char)
        else:
            # If the character is not alphabetic, keep it unchanged
            decrypted_text.append(char)
    
    # Join the list of characters into a single string and return the decrypted text
    return ''.join(decrypted_text)

# Example usage:
plaintext = "Jimit chavda"
key = "KEY"

# Encrypt the plaintext using the Vigenère cipher
ciphertext = vigenere_encrypt(plaintext, key)
print(f"Encrypted: {ciphertext}")

# Decrypt the ciphertext back to the original plaintext
decrypted_text = vigenere_decrypt(ciphertext, key)
print(f"Decrypted: {decrypted_text}")
