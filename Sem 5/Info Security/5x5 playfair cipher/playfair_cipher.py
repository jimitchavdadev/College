import string

# matrix generation code block

def generate_playfair_matrix(key):
    # we use set because it removes the duplicate entries
    # using lambda to sort the characters in their original order rather than some random order
    key = "".join(sorted(set(key), key=lambda x: key.index(x)))  # Remove duplicates while preserving order
    
    # storing all ascii uppercase letters but omitting J     
    alphabet = string.ascii_uppercase.replace("J", "")  # Playfair cipher traditionally omits 'J'
    
    # further we just store all the characters in key which are not present in the key 
    key += ''.join([char for char in alphabet if char not in key])
    
    matrix = []
    char_positions = {}  # Dictionary to store character coordinates
    for i in range(5):
    # storing the slices of keys in an order of 5 keys
    # ex- 0-5, 5-10 etc.
        row = key[i*5:(i+1)*5]
        matrix.append(list(row))
        for j in range(5):
            char_positions[row[ j]] = (i, j)  # Store the coordinates
    
    return matrix, char_positions

def format_plaintext(plaintext):
    # converting all plaintext to uppercase and removing J with I and remove space in the string
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    formatted_text = ""
    
    i = 0
    while i < len(plaintext):
        formatted_text += plaintext[i]
        # if two consecutive letters are same it will replace the next one with 'X'
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
            formatted_text += "X"
        elif i + 1 < len(plaintext):
            formatted_text += plaintext[i + 1]
            i += 1
        i += 1
        
        # if formatted string is in odd length we have to change it to even length
        # we need even length string to make diagraphs
    if len(formatted_text) % 2 != 0:
        formatted_text += "X"
    return formatted_text

def playfair_encrypt(plaintext, matrix, char_positions):
    ciphertext = ""
    
    for i in range(0, len(plaintext), 2):
        # extracting coordinates from the dictionary for two consecutive letters
        row1, col1 = char_positions[plaintext[i]]
        row2, col2 = char_positions[plaintext[i + 1]]
        
        # if letters are in same row then move it by forward one unit in the column
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
    
        # if letters are in same column then move it forward by one unit in the row
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
    
        else:
        # if not present in the same row/column, replace it with diagonally opposite letters in the matrix
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]
    
    return ciphertext

def playfair_decrypt(ciphertext, matrix, char_positions):
    plaintext = ""
    
    for i in range(0, len(ciphertext), 2):
        row1, col1 = char_positions[ciphertext[i]]
        row2, col2 = char_positions[ciphertext[i + 1]]
        
        # if letters are in same row then move it backwards by one unit in the column
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]

        # if letters are in same column then move it backwards by one unit in the row
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
    
        else:
        # diagonally exchange the elements
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]
    
    return plaintext

# main block 

def main():
    while True:
        choice = input("Do you want to Encrypt (E), Decrypt (D), or Quit (Q)? ").upper()
        if choice == 'Q':
            break
        elif choice in ['E', 'D']:
            # converting the string in upper case by default
            key = input("Enter the keyword: ").upper()
            text = input("Enter the text: ").upper()
            
            # matrix -> list, char_positions -> dict
            matrix, char_positions = generate_playfair_matrix(key)
            
            if choice == 'E':
                formatted_text = format_plaintext(text)
                result = playfair_encrypt(formatted_text, matrix, char_positions)
                print(f"Encrypted Text: {result}")
    
            elif choice == 'D':
                result = playfair_decrypt(text, matrix, char_positions)
                print(f"Decrypted Text: {result}")
        else:
            print("Invalid choice. Please enter E for Encrypt, D for Decrypt, or Q for Quit.")

if __name__ == "__main__":
    main()
