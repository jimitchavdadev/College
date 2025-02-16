import numpy as np
import random

# Function to save a matrix to a text file
def save_matrix_to_file(matrix, filename):
    # Save the matrix to a file with integers format
    np.savetxt(filename, matrix, fmt='%d')

# Function to load a matrix from a text file
def load_matrix_from_file(filename):
    # Load the matrix from the file with integer type
    return np.loadtxt(filename, dtype=int)

# Function to generate a random matrix of a given size that is invertible mod 26
def generate_random_matrix(size, modulus):
    while True:
        # Generate a random matrix with values between 0 and the modulus (26)
        matrix = np.random.randint(0, modulus, size=(size, size))
        # Calculate the determinant of the matrix
        det = int(np.round(np.linalg.det(matrix)))
        # Ensure the determinant is coprime with the modulus (26) for invertibility
        if np.gcd(det, modulus) == 1:
            return matrix

# Function to calculate the modular inverse of a matrix under a given modulus (26)
def mod_matrix_inverse(matrix, modulus):
    # Calculate the determinant of the matrix and round it to avoid precision issues
    det = int(np.round(np.linalg.det(matrix)))
    # Calculate the modular inverse of the determinant mod 26
    det_inv = pow(det, -1, modulus)
    # Calculate the matrix inverse, scale by determinant inverse, and apply mod 26
    matrix_mod_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return matrix_mod_inv

# Function to encrypt a message using the Hill cipher with an additional random matrix
def hill_encrypt(message, key_matrix, random_matrix):
    # Convert the message characters to corresponding numbers (A=0, B=1, ..., Z=25)
    message_numbers = [ord(char) - ord('A') for char in message.upper()]
    
    # If the message length is odd, pad it with 'X' to ensure even length
    if len(message_numbers) % 2 != 0:
        message_numbers.append(ord('X') - ord('A'))
    
    # Reshape the message numbers into a 2xN matrix for encryption
    message_matrix = np.array(message_numbers).reshape(-1, 2).T
    
    # Multiply the message matrix with the random matrix, then apply modulus 26
    intermediate_matrix = np.dot(random_matrix, message_matrix) % 26
    # Multiply the resulting matrix with the key matrix and apply modulus 26
    encrypted_matrix = np.dot(key_matrix, intermediate_matrix) % 26
    
    # Convert the resulting numbers back to letters to form the encrypted message
    encrypted_message = ''.join(chr(num + ord('A')) for num in encrypted_matrix.T.flatten())
    
    return encrypted_message

# Function to decrypt a message using the Hill cipher with an additional random matrix
def hill_decrypt(encrypted_message, key_matrix, random_matrix):
    # Convert the encrypted message characters back to numbers (A=0, B=1, ..., Z=25)
    encrypted_numbers = [ord(char) - ord('A') for char in encrypted_message.upper()]
    
    # Reshape the encrypted numbers into a 2xN matrix for decryption
    encrypted_matrix = np.array(encrypted_numbers).reshape(-1, 2).T
    
    # Calculate the modular inverse of the key matrix for decryption
    key_matrix_inv = mod_matrix_inverse(key_matrix, 26)
    # Calculate the modular inverse of the random matrix for decryption
    random_matrix_inv = mod_matrix_inverse(random_matrix, 26)
    
    # Multiply the encrypted matrix with the inverse key matrix and apply modulus 26
    intermediate_matrix = np.dot(key_matrix_inv, encrypted_matrix) % 26
    # Multiply the resulting matrix with the inverse random matrix and apply modulus 26
    decrypted_matrix = np.dot(random_matrix_inv, intermediate_matrix) % 26
    
    # Convert the resulting numbers back to letters to form the decrypted message
    decrypted_message = ''.join(chr(int(num) + ord('A')) for num in decrypted_matrix.T.flatten())
    
    return decrypted_message

# Main program to handle user input and perform encryption or decryption
def main():
    # Define the filename to save and load the random matrix
    filename = "random_matrix.txt"
    # Define a fixed key matrix for encryption (2x2 matrix)
    key_matrix = np.array([[3, 3], [2, 5]])
    
    # Prompt the user to choose between encryption and decryption
    choice = input("Choose 'encrypt' or 'decrypt': ").strip().lower()
    
    if choice == 'encrypt':
        # Get the plaintext message to encrypt from the user
        message = input("Enter the message to encrypt: ").strip().upper()
        
        # Generate a random 2x2 matrix for encryption and save it to a file
        random_matrix = generate_random_matrix(2, 26)
        save_matrix_to_file(random_matrix, filename)
        
        # Encrypt the message using the Hill cipher and the random matrix
        encrypted_message = hill_encrypt(message, key_matrix, random_matrix)
        print(f"Encrypted message: {encrypted_message}")
    
    elif choice == 'decrypt':
        # Get the encrypted message to decrypt from the user
        encrypted_message = input("Enter the message to decrypt: ").strip().upper()
        
        # Load the random matrix from the file for decryption
        random_matrix = load_matrix_from_file(filename)
        
        # Decrypt the message using the Hill cipher and the random matrix
        decrypted_message = hill_decrypt(encrypted_message, key_matrix, random_matrix)
        print(f"Decrypted message: {decrypted_message}")
    
    else:
        # Print an error message if the user makes an invalid choice
        print("Invalid choice. Please choose 'encrypt' or 'decrypt'.")

# Run the main program when the script is executed
if __name__ == "__main__":
    main()
