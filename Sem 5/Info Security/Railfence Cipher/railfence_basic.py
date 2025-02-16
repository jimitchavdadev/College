def rail_fence_encrypt(text, key):
    # Create an empty matrix to store the text
    rail = [['\n' for _ in range(len(text))]
                  for _ in range(key)]
     
    # Direction controls
    dir_down = False
    row, col = 0, 0
     
    # Fill the rail matrix
    for char in text:
        # Check if we need to change direction
        if row == 0 or row == key - 1:
            dir_down = not dir_down
         
        # Place the character
        rail[row][col] = char
        col += 1
         
        # Move to the next row
        row += 1 if dir_down else -1
     
    # Read the matrix in row-major order to get the encrypted text
    encrypted_text = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                encrypted_text.append(rail[i][j])
    return "".join(encrypted_text)
