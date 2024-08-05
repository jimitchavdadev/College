
def find_position(char, key_square):
    for i, row in enumerate(key_square):
        for j, letter in enumerate(row):
            if char == letter:
                return i, j
    return None

def playfair_encrypt(plaintext, key):
    key_square = generate_key_square(key)
    plaintext = format_plaintext(plaintext)
    ciphertext = ""
    
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        row_a, col_a = find_position(a, key_square)
        row_b, col_b = find_position(b, key_square)
        
        if row_a == row_b:
            ciphertext += key_square[row_a][(col_a + 1) % 5]
            ciphertext += key_square[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            ciphertext += key_square[(row_a + 1) % 5][col_a]
            ciphertext += key_square[(row_b + 1) % 5][col_b]
        else:
            ciphertext += key_square[row_a][col_b]
            ciphertext += key_square[row_b][col_a]
    
    return ciphertext

# Example usage:
key = "playfair example"
plaintext = "Hide the gold in the tree stump"
ciphertext = playfair_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
