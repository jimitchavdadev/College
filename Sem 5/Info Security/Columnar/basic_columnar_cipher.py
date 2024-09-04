import math

def encrypt(key, plaintext):
    ciphertext = ""
    key_len = len(key)
    
    # Calculate number of rows and columns in the matrix
    num_rows = math.ceil(len(plaintext) / key_len)
    num_cols = key_len
    
    # Create the matrix to store plaintext
    matrix = [[''] * num_cols for _ in range(num_rows)]
    
    # Populate the matrix row-wise with plaintext
    row, col = 0, 0
    for char in plaintext:
        matrix[row][col] = char
        row += 1
        if row == num_rows:
            row = 0
            col += 1
    
    # Extract ciphertext column-wise using the key
    key_indexes = sorted(range(len(key)), key=lambda i: key[i])
    for j in key_indexes:
        for i in range(num_rows):
            if matrix[i][j] != '':
                ciphertext += matrix[i][j]
    
    return ciphertext

def decrypt(key, ciphertext):
    plaintext = ""
    key_len = len(key)
    
    # Calculate number of rows and columns in the matrix
    num_rows = math.ceil(len(ciphertext) / key_len)
    num_cols = key_len
    
    # Create the matrix to store ciphertext
    matrix = [[''] * num_cols for _ in range(num_rows)]
    
    # Populate the matrix column-wise using the key
    key_indexes = sorted(range(len(key)), key=lambda i: key[i])
    col = 0
    for j in key_indexes:
        for i in range(num_rows):
            matrix[i][j] = ciphertext[col]
            col += 1
    
    # Extract plaintext row-wise from the matrix
    row, col = 0, 0
    for _ in range(len(ciphertext)):
        plaintext += matrix[row][col]
        row += 1
        if row == num_rows:
            row = 0
            col += 1
    
    return plaintext

key = "HACK"
plaintext = "HELLO WORLD"
ciphertext = encrypt(key, plaintext)
print("Ciphertext:", ciphertext)  # Output: Ciphertext: HOLEWDLR OL
decrypted_text = decrypt(key, ciphertext)
print("Decrypted text:", decrypted_text)  # Output: Decrypted text: HELLO WORLD