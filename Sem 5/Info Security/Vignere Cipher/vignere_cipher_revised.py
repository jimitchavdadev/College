# Define a custom alphabet including 26 letters and 10 special characters
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
ALPHABET_LENGTH = len(ALPHABET)

# Create a dictionary for fast index lookup
INDEX = {char: idx for idx, char in enumerate(ALPHABET)}

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


def reverse_and_extend_key(key, length):
    # Reverse the key and extend it to match the length
    reversed_key = key[::-1]
    repeated_key = (reversed_key * (length // len(reversed_key))) + reversed_key[:length % len(reversed_key)]
    return repeated_key

def encrypt_decrypt(text, key, mode='encrypt'):
    # Extend the key to the length of the text
    extended_key = reverse_and_extend_key(key, len(text)).upper()
    
    # List to store the encrypted or decrypted characters
    result = []
    
    for i, char in enumerate(text):
        if char in INDEX:
            # Get the index for the current character and the key character
            char_idx = INDEX[char]
            key_idx = INDEX[extended_key[i % len(extended_key)]]
            
            if mode == 'encrypt':
                # Encrypt the character
                new_idx = (char_idx + key_idx) % ALPHABET_LENGTH
            elif mode == 'decrypt':
                # Decrypt the character
                new_idx = (char_idx - key_idx) % ALPHABET_LENGTH
            
            result.append(ALPHABET[new_idx])
        else:
            # If the character is not in the alphabet, add it unchanged
            result.append(char)
    
    return ''.join(result)

def vigenere_encrypt(plaintext, key):
    return encrypt_decrypt(plaintext, key, mode='encrypt')

def vigenere_decrypt(ciphertext, key):
    return encrypt_decrypt(ciphertext, key, mode='decrypt')

def main():
    # Ask the user whether they want to encrypt or decrypt
    action = input("Would you like to (E)ncrypt or (D)ecrypt? ").strip().upper()
    
    if action == 'E':
        key = input("Enter the key: ").strip()
        # If the user wants to encrypt, get the plaintext
        plaintext = input("Enter the plaintext: ").strip().upper()
        # Encrypt the plaintext using the Vigenère cipher
        ciphertext = vigenere_encrypt(plaintext, key)
        print(f"Encrypted: {ciphertext}")
    elif action == 'D':
        key = reverse(input("Enter the key: ").strip())
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
