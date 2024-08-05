alphabets = list("abcdefghijklmnopqrstuvwxyz")
matrix = []
key = "hello world"

def generate_matrix(key):
    key = "".join(sorted(set(key), key=key.index))  # Remove duplicates while preserving order
    key = key.replace(" ", "")  # Remove spaces from the key
    key = key.lower()  # Ensure the key is in lowercase
    
    # Remove key characters from alphabets
    for char in key:
        if char in alphabets:
            alphabets.remove(char)
    
    # Create the matrix
    for char in key + "".join(alphabets):
        if char=='j':
            continue
        
        if char not in [c for row in matrix for c in row]:
            if len(matrix) == 0 or len(matrix[-1]) == 5:
                matrix.append([])
            matrix[-1].append(char)
    
generate_matrix(key)


diagraphs = []

def create_diagraphs(key):
    # Remove non-alphabetic characters and convert to lowercase
    key = "".join(filter(str.isalpha, key)).lower()
    
    i = 0
    while i < len(key):
        # Take two characters at a time
        if i + 1 < len(key):
            if key[i] == key[i + 1]:
                # If two characters are the same, insert a filler character
                diagraphs.append(key[i] + 'x')
                i += 1
            else:
                diagraphs.append(key[i] + key[i + 1])
                i += 2
        else:
            # If there's a single character left, pair it with a filler character
            diagraphs.append(key[i] + 'x')
            i += 1

key = "hello world"
create_diagraphs(key)

def find_position(char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None, None

def encrypt_diagraphs(diagraphs):
    result = ""
    for diagraph in diagraphs:
        r1, c1 = find_position(diagraph[0])
        r2, c2 = find_position(diagraph[1])
        
        if r1 == r2:
            # Same row
            result += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            # Same column
            result += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else:
            # Rectangle
            result += matrix[r1][c2] + matrix[r2][c1]
    
    return result

# Main
generate_matrix(key)
diagraphs = []
create_diagraphs(key)
encrypted_text = encrypt_diagraphs(diagraphs)
print(f"Matrix: ")
for i in matrix: 
    print(i)

print(f"Diagraphs: {diagraphs}")
print(f"Encrypted Text: {encrypted_text}")