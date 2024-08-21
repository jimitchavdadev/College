def reverse_and_shift_key(key):
    # Reverse the given key string
    reversed_key = key[::-1]
    
    # Calculate the length of the key
    key_length = len(key)
    
    # Create a new string where each character in the reversed key is shifted backward by the length of the key
    shifted_key = ''.join(
        # For each character in the reversed key
        chr((ord(char) - ord('A') - key_length) % 26 + ord('A'))  # Shift it backward and wrap around if necessary
        for char in reversed_key
    )
    return shifted_key

def vigenere_encrypt(plaintext, key):
    # Transform the key by reversing and shifting it
    key = reverse_and_shift_key(key).upper()
    
    # Calculate the length of the plaintext
    plaintext_length = len(plaintext)
    
    # List to store the encrypted characters
    encrypted_text = []
    
    # Iterate over each character in the plaintext
    for i, char in enumerate(plaintext):
        if char.isalpha():  # Check if the character is alphabetic
            # Calculate the shift amount based on the length of the plaintext
            shift = plaintext_length
            
            # Calculate the shift amount for the corresponding key character
            key_shift = ord(key[i % len(key)]) - ord('A')
            
            if char.isupper():  # Check if the character is uppercase
                # Encrypt the character by shifting it forward in the alphabet
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:  # The character is lowercase
                # Encrypt the character by shifting it forward in the alphabet
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            
            encrypted_text.append(encrypted_char)  # Append the encrypted character to the list
        else:
            # If the character is not alphabetic, add it unchanged
            encrypted_text.append(char)
    
    # Join the list of characters into a single string and return it
    return ''.join(encrypted_text)

def vigenere_decrypt(ciphertext, key):
    # Transform the key by reversing and shifting it
    key = reverse_and_shift_key(key).upper()
    
    # Calculate the length of the ciphertext
    ciphertext_length = len(ciphertext)
    
    # List to store the decrypted characters
    decrypted_text = []
    
    # Iterate over each character in the ciphertext
    for i, char in enumerate(ciphertext):
        if char.isalpha():  # Check if the character is alphabetic
            # Calculate the shift amount based on the length of the ciphertext
            shift = ciphertext_length
            
            # Calculate the shift amount for the corresponding key character
            key_shift = ord(key[i % len(key)]) - ord('A')
            
            if char.isupper():  # Check if the character is uppercase
                # Decrypt the character by shifting it backward in the alphabet
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:  # The character is lowercase
                # Decrypt the character by shifting it backward in the alphabet
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            
            decrypted_text.append(decrypted_char)  # Append the decrypted character to the list
        else:
            # If the character is not alphabetic, add it unchanged
            decrypted_text.append(char)
    
    # Join the list of characters into a single string and return it
    return ''.join(decrypted_text)

def main():
    # Ask the user whether they want to encrypt or decrypt
    action = input("Would you like to (E)ncrypt or (D)ecrypt? ").strip().upper()
    
    # Get the key from the user
    key = input("Enter the key: ").strip()
    
    if action == 'E':
        # If the user wants to encrypt, get the plaintext
        plaintext = input("Enter the plaintext: ").strip()
        # Encrypt the plaintext using the Vigenère cipher
        ciphertext = vigenere_encrypt(plaintext, key)
        print(f"Encrypted: {ciphertext}")
    elif action == 'D':
        # If the user wants to decrypt, get the ciphertext
        ciphertext = input("Enter the ciphertext: ").strip()
        # Decrypt the ciphertext using the Vigenère cipher
        decrypted_text = vigenere_decrypt(ciphertext, key)
        print(f"Decrypted: {decrypted_text}")
    else:
        # If the user input is invalid, print an error message
        print("Invalid choice. Please choose 'E' to encrypt or 'D' to decrypt.")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
