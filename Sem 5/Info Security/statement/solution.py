"""
Design cipher with detailed explanation. Sample as
follows.


a) Write a program to encrypt the plaintext with the
given key. E.g. plaintext GRONSFELD with the
key 1234. Add 1 to G to get H (the letter 1 rank
after G is H in the alphabet), then add 2 to C or
E (the letter 2 ranks after C is E), and so on. Use
smallest letter from plaintext as filler.
b) Encrypt the input words PLAINTEXT= RAG
BABY to obtain CIPHERTEXT = SCJ DDFDZ
"""

def encrypt(plaintext, key):
    # Convert plaintext to uppercase and remove non-alpha characters
    plaintext = ''.join(filter(str.isalpha, plaintext.upper()))
    key = [int(k) for k in str(key)]  # Convert key to a list of integers
    key_length = len(key)
    
    # Fill the plaintext with the smallest letter if necessary
    while len(plaintext) % key_length != 0:
        smallest_letter = min(plaintext)
        plaintext += smallest_letter
    
    ciphertext = []
    
    for i, char in enumerate(plaintext):
        # Calculate the new character based on the key
        shift = key[i % key_length]
        new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        ciphertext.append(new_char)
    
    return ''.join(ciphertext)

# Example usage
plaintext1 = "GRONSFELD"
key1 = 1234
ciphertext1 = encrypt(plaintext1, key1)
print(f"Ciphertext for '{plaintext1}' with key '{key1}': {ciphertext1}")

# Encrypting RAG BABY
plaintext2 = "RAG BABY"
key2 = 1234  # Using the same key for simplicity
ciphertext2 = encrypt(plaintext2, key2)
print(f"Ciphertext for '{plaintext2}' with key '{key2}': {ciphertext2}")