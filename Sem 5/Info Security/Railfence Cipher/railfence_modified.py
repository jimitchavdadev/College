def encrypt_non_uniform_rail_fence(text, key_pattern):
    # Remove spaces and convert text to uppercase for simplicity
    text = text.replace(" ", "").upper()
    
    # Create a list of empty strings for each rail based on the maximum number of rails in key_pattern
    rails = ['' for _ in range(max(key_pattern))]
    
    # Initialize the rail index and direction for zigzag traversal
    rail_index = 0
    direction_down = True
    
    # Iterate through each character in the text
    for i, char in enumerate(text):
        # Append the character to the current rail
        rails[rail_index] += char
        
        # Update rail index based on current direction
        if direction_down:
            rail_index += 1
        else:
            rail_index -= 1
        
        # Check if the rail index has reached the bottom or top to change direction
        if rail_index == key_pattern[i % len(key_pattern)] - 1:
            direction_down = False
        elif rail_index == 0:
            direction_down = True
    
    # Concatenate all rails to get the final encrypted text
    return ''.join(rails)

def decrypt_non_uniform_rail_fence(cipher, key_pattern):
    # Create a list to store the number of characters in each rail
    rail_lengths = [0 for _ in range(max(key_pattern))]
    
    # Determine the number of characters in each rail based on the zigzag pattern
    rail_index = 0
    direction_down = True
    for i in range(len(cipher)):
        # Increment the character count for the current rail
        rail_lengths[rail_index] += 1
        
        # Update rail index based on current direction
        if direction_down:
            rail_index += 1
        else:
            rail_index -= 1
        
        # Check if the rail index has reached the bottom or top to change direction
        if rail_index == key_pattern[i % len(key_pattern)] - 1:
            direction_down = False
        elif rail_index == 0:
            direction_down = True
    
    # Create a list of strings to hold the characters of each rail
    rails = ['' for _ in range(max(key_pattern))]

    # Fill the rails with characters from the cipher text
    index = 0
    for rail in range(max(key_pattern)):
        rails[rail] = cipher[index:index + rail_lengths[rail]]
        index += rail_lengths[rail]
    
    # Reconstruct the original message by following the zigzag pattern
    result = []
    rail_index = 0
    direction_down = True
    rail_pointers = [0 for _ in range(max(key_pattern))]
    
    # Iterate through each character position in the cipher text
    for i in range(len(cipher)):
        # Append the current character from the rail to the result
        result.append(rails[rail_index][rail_pointers[rail_index]])
        rail_pointers[rail_index] += 1
        
        # Update rail index based on current direction
        if direction_down:
            rail_index += 1
        else:
            rail_index -= 1
        
        # Check if the rail index has reached the bottom or top to change direction
        if rail_index == key_pattern[i % len(key_pattern)] - 1:
            direction_down = False
        elif rail_index == 0:
            direction_down = True
    
    # Return the decrypted message as a single string
    return ''.join(result)

# Example usage:
message = "HELLO AHMEDABAD"
key_pattern = [2, 4, 3]

# Encrypt the message using the non-uniform rail fence cipher
cipher_text = encrypt_non_uniform_rail_fence(message, key_pattern)
print("Encrypted:", cipher_text)

# Decrypt the cipher text to retrieve the original message
decrypted_text = decrypt_non_uniform_rail_fence(cipher_text, key_pattern)
print("Decrypted:", decrypted_text)
