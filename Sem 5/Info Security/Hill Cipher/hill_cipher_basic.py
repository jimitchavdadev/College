import numpy as np

def mod_matrix_inverse(matrix, modulus):
    """
    Calculate the modular inverse of a given matrix.
    """
    # Compute the determinant of the matrix and round it to ensure it's an integer
    det = int(np.round(np.linalg.det(matrix)))
    
    # Find the modular inverse of the determinant under the given modulus (usually 26)
    det_inv = pow(det, -1, modulus)
    
    # Calculate the matrix inverse, multiply by the determinant's inverse, and apply modulus
    # This gives us the modular inverse of the matrix
    matrix_mod_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    
    return matrix_mod_inv

def hill_encrypt(message, key_matrix):
    """
    Encrypt a message using the Hill cipher method.
    """
    # Convert each character in the message to its corresponding numeric value (A=0, B=1, ..., Z=25)
    message_numbers = [ord(char) - ord('A') for char in message.upper()]
    
    # If the message length is odd, pad it with 'X' (value 23) to ensure even length
    if len(message_numbers) % 2 != 0:
        message_numbers.append(ord('X') - ord('A'))
    
    # Reshape the message numbers into a 2xN matrix where each column is a pair of letters
    message_matrix = np.array(message_numbers).reshape(-1, 2).T
    
    # Multiply the key matrix by the message matrix to encrypt it, then apply modulus 26
    encrypted_matrix = np.dot(key_matrix, message_matrix) % 26
    
    # Convert the encrypted numeric values back to letters and concatenate them into a string
    encrypted_message = ''.join(chr(num + ord('A')) for num in encrypted_matrix.T.flatten())
    
    return encrypted_message

def hill_decrypt(encrypted_message, key_matrix):
    """
    Decrypt a message encrypted using the Hill cipher method.
    """
    # Convert the encrypted message back to numeric values (A=0, B=1, ..., Z=25)
    encrypted_numbers = [ord(char) - ord('A') for char in encrypted_message.upper()]
    
    # Reshape the encrypted numbers into a 2xN matrix, similar to how the message was processed
    encrypted_matrix = np.array(encrypted_numbers).reshape(-1, 2).T
    
    # Calculate the inverse of the key matrix under modulus 26 for decryption
    key_matrix_inv = mod_matrix_inverse(key_matrix, 26)
    
    # Multiply the inverse key matrix by the encrypted matrix to decrypt it, then apply modulus 26
    decrypted_matrix = np.dot(key_matrix_inv, encrypted_matrix) % 26
    
    # Convert the decrypted numeric values back to letters and concatenate them into a string
    decrypted_message = ''.join(chr(int(num) + ord('A')) for num in decrypted_matrix.T.flatten())
    
    return decrypted_message

# Example usage of the Hill cipher

# Define the encryption key matrix (2x2 matrix)
key_matrix = np.array([[3, 3], [2, 5]])  # This matrix should be invertible mod 26

# Define the message to encrypt
message = "HELLO"

# Encrypt the message using the Hill cipher
encrypted_message = hill_encrypt(message, key_matrix)
print(f"Encrypted message: {encrypted_message}")

# Decrypt the message back to the original text
decrypted_message = hill_decrypt(encrypted_message, key_matrix)
print(f"Decrypted message: {decrypted_message}")
