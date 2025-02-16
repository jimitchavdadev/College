import math
import numpy as np
import json
import random
import string

# Define the JSON file to store the keys
KEYS_FILE = 'keys.json'

def generate_random_key():
    alphabet = string.ascii_lowercase
    indices = list(range(len(alphabet)))
    random.shuffle(indices)
    return dict(zip(alphabet, indices))

def save_key_to_json(key):
    with open(KEYS_FILE, 'w') as f:
        json.dump(key, f)

def load_key_from_json():
    try:
        with open(KEYS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def columnar_matrix(text, key):
    # Determine the number of rows needed in the matrix.
    num_rows = math.ceil(len(text) / len(key))
    
    # Initialize the matrix with placeholder characters ('_') for empty spaces.
    text_mat = np.full((num_rows, len(key)), '_', dtype='<U1')
    
    # Populate the matrix with characters from the text.
    for i in range(len(text)):
        row = i // len(key)  # Determine the current row index.
        col = i % len(key)   # Determine the current column index.
        text_mat[row, col] = text[i]  # Place the text character in the matrix.
    
    return text_mat

def columnar_encrypt(text, key):
    # Create the matrix from the text and key.
    text_mat = columnar_matrix(text, key)
    
    # Create a list of column indices based on the key and sort them according to the key characters.
    key_order = list(range(len(key)))  # Original order of columns.
    key_list = list(key)  # Convert the key into a list of characters.
    combined_list = zip(key_list, key_order)  # Pair each key character with its column index.
    sorted_key_list, sorted_order = zip(*sorted(combined_list, key=lambda x: x[0]))  # Sort columns based on key characters.

    # Initialize an empty string to hold the encrypted text.
    encrypted_text = ''

    # Read the matrix column by column according to the sorted order and concatenate characters to form the encrypted text.
    for i in sorted_order:
        for j in range(math.ceil(len(text) / len(key))):
            encrypted_text += text_mat[j, i]
    
    return encrypted_text

def columnar_decrypt(text, key):
    # Create the matrix for decryption.
    num_rows = math.ceil(len(text) / len(key))
    text_mat = np.full((num_rows, len(key)), '_', dtype='<U1')
    
    # Create a list of column indices based on the key and sort them according to the key characters.
    key_order = list(range(len(key)))  # Original order of columns.
    key_list = list(key)  # Convert the key into a list of characters.
    combined_list = zip(key_list, key_order)  # Pair each key character with its column index.
    sorted_key_list, sorted_order = zip(*sorted(combined_list, key=lambda x: x[0]))  # Sort columns based on key characters.

    # Initialize an empty string to hold the decrypted text.
    decrypted_text = ''
    index = 0  # Index to track the position in the encrypted text.

    # Fill the matrix with the encrypted text characters according to the sorted column order.
    for i in sorted_order:
        for j in range(num_rows):
            if index < len(text):
                text_mat[j, i] = text[index]
                index += 1
    
    # Read the matrix row by row and concatenate characters to form the decrypted text.
    for i in range(len(text)):
        if text_mat[i // len(key), i % len(key)] != '_':
            decrypted_text += text_mat[i // len(key), i % len(key)]

    return decrypted_text

if __name__ == '__main__':
    plain = "Hello world"
    key = "key"

    # Check if the key file exists; if not, generate a new key and save it.
    key_mapping = load_key_from_json()
    if key_mapping is None:
        key_mapping = generate_random_key()
        save_key_to_json(key_mapping)

    # Map the key to the generated indices.
    key = ''.join(sorted(key_mapping.keys(), key=lambda k: key_mapping[k]))

    # Test the functions with sample data.
    matrix = columnar_matrix(plain, key)
    print("Matrix:")
    print(matrix)
    print()
    
    encrypted = columnar_encrypt(plain, key)
    print("Encrypted:")
    print(encrypted)
    
    decrypted = columnar_decrypt(encrypted, key)
    print("Decrypted:")
    print(decrypted)
