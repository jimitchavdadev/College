import numpy as np

def text_to_matrix(text, size):
    # Convert the text to a matrix of given size
    return np.array([ord(char) - ord('A') for char in text.upper()]).reshape(-1, size)

def matrix_to_text(matrix):
    # Convert matrix to text
    return ''.join(chr(int(num) + ord('A')) for num in matrix.flatten())

def permute_matrix(matrix, perm):
    # Apply permutation to the rows of the matrix
    return matrix[perm]

def create_permutation_matrix(size):
    # Create a permutation matrix to shuffle rows
    perm = np.random.permutation(size)
    return perm

def encrypt_hill_cipher(plaintext, key_matrix):
    # Ensure key matrix is square
    size = key_matrix.shape[0]

    # Prepare plaintext matrix with space replaced by nothing
    padded_text = plaintext.upper().replace(' ', '')

    # Pad the text with filler characters to match the size of nxn matrix
    if len(padded_text) % size != 0:
        padded_text += 'X' * (size - len(padded_text) % size)

    # Change the plaintext into the nxn matrix
    plaintext_matrix = text_to_matrix(padded_text, size)
    
    # Create a permutation matrix
    perm = create_permutation_matrix(size)
    
    # Apply the permutation matrix to the plaintext matrix
    permuted_plaintext_matrix = permute_matrix(plaintext_matrix, perm)

    # Encrypt
    ciphertext_matrix = (np.dot(permuted_plaintext_matrix, key_matrix) % 26)

    # Convert to text
    ciphertext = matrix_to_text(ciphertext_matrix)

    return ciphertext

# Define a key matrix for the Hill cipher
key_matrix = np.array([[6, 24], [1, 8]])

# Define the plaintext to encrypt
plaintext = "HELLO WORLD"

# Encrypt the plaintext using the Hill cipher
ciphertext = encrypt_hill_cipher(plaintext, key_matrix)

print("Ciphertext: ", ciphertext)
