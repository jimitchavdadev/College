import string

# function to create the key matrix using the keyword
def create_matrix(keyword):
    keyword = "".join(dict.fromkeys(keyword))  # remove duplicates
    keyword = keyword.replace("J", "I").upper()  # treat 'J' as 'I' and uppercase
    alphabet = string.ascii_uppercase.replace("J", "")
    
    key_matrix = []
    used_chars = set()

    for char in keyword:
        if char not in used_chars:
            key_matrix.append(char)
            used_chars.add(char)
    
    for char in alphabet:
        if char not in used_chars:
            key_matrix.append(char)
            used_chars.add(char)
    
    matrix = [key_matrix[i:i+5] for i in range(0, 25, 5)]  # create 5x5 matrix
    return matrix

# function to preprocess the text
def preprocess_text(text):
    text = text.upper().replace("J", "I")  # replace 'J' with 'I' and convert to uppercase
    processed_text = ""

    i = 0
    while i < len(text):
        if text[i] not in string.ascii_uppercase:  # skip non-alphabet characters
            i += 1
            continue
        processed_text += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed_text += "X"  # insert 'X' between duplicate letters
        elif i + 1 < len(text) and text[i + 1] in string.ascii_uppercase:
            processed_text += text[i + 1]
            i += 1
        i += 1

    if len(processed_text) % 2 != 0:
        processed_text += "X"  # add 'X' if the length is odd

    return processed_text

# function to find the position of a character in the matrix
def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, matrix_char in enumerate(row):
            if matrix_char == char:
                return i, j
    return None

# function to perform playfair cipher encryption or decryption
def playfair_cipher(text, matrix, mode='encrypt'):
    text = preprocess_text(text)
    result = ""

    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        
        if row1 is None or row2 is None:
            raise ValueError(f"Characters {char1} or {char2} not found in matrix")

        if row1 == row2:  # same row
            if mode == 'encrypt':
                result += matrix[row1][(col1 + 1) % 5]
                result += matrix[row2][(col2 + 1) % 5]
            else:
                result += matrix[row1][(col1 - 1) % 5]
                result += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # same column
            if mode == 'encrypt':
                result += matrix[(row1 + 1) % 5][col1]
                result += matrix[(row2 + 1) % 5][col2]
            else:
                result += matrix[(row1 - 1) % 5][col1]
                result += matrix[(row2 - 1) % 5][col2]
        else:  # rectangle swap
            result += matrix[row1][col2]
            result += matrix[row2][col1]

    return result

# function to encrypt plaintext using playfair cipher
def encrypt(plaintext, keyword):
    matrix = create_matrix(keyword)
    return playfair_cipher(plaintext, matrix, 'encrypt')

# function to decrypt ciphertext using playfair cipher
def decrypt(ciphertext, keyword):
    matrix = create_matrix(keyword)
    return playfair_cipher(ciphertext, matrix, 'decrypt')

# example usage
keyword = "playfair"
plaintext = "hide the gold in the tree stump"
ciphertext = encrypt(plaintext, keyword)
decrypted_text = decrypt(ciphertext, keyword)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)
