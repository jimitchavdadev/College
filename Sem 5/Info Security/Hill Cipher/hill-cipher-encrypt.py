import numpy as np

def text_to_matrix(text, size):
    # we use reshape to give the size of the matrix 
    # we use -1 as index so that it calculates the size based on the remaining dimensions
    return np.array([ord(char) - ord('A') for char in text.upper()]).reshape(-1, size)

def matrix_to_text(matrix):
    # flatten converts the matrix intro a 1D string
    return ''.join(chr(int(num) + ord('A')) for num in matrix.flatten())

def encrypt_hill_cipher(plaintext, key_matrix):
    # length of the key matrix
    size = key_matrix.shape[0]
    
    # Prepare plaintext matrix with space replaced by nothing
    padded_text = plaintext.upper().replace(' ', '') 

    # we will pad the text with filler characters to match the size of nxn matrix
    if len(padded_text) % size != 0:
        padded_text += 'X' * (size - len(padded_text) % size) 
    
    # we will change the plaintext into the nxn matrix 
    plaintext_matrix = text_to_matrix(padded_text, size)
    
    # Encrypt
    ciphertext_matrix = (np.dot(plaintext_matrix, key_matrix) % 26)
    
    # Convert to text
    ciphertext = matrix_to_text(ciphertext_matrix)
    
    return ciphertext

key_matrix = np.array([[6,24],[1,8]])

plaintext="HELLO WORLD"
ciphertext=encrypt_hill_cipher(plaintext, key_matrix)
print("Ciphertext: ", ciphertext)