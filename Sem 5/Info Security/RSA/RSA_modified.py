import random

# Function to find the greatest common divisor (gcd)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to compute modular inverse using the Extended Euclidean Algorithm
def mod_inverse(e, phi):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x
    
    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % phi

# Function to generate RSA keys with CRT optimization
def generate_keys():
    # Step 1: Choose two large prime numbers
    p = 61
    q = 53
    n = p * q
    
    # Step 2: Compute φ(n) = (p - 1) * (q - 1)
    phi = (p - 1) * (q - 1)
    
    # Step 3: Choose e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
    e = random.choice([i for i in range(2, phi) if gcd(i, phi) == 1])
    
    # Step 4: Compute d as the modular inverse of e mod φ(n)
    d = mod_inverse(e, phi)
    
    # Precompute values for CRT optimization
    dp = d % (p - 1)  # d mod (p - 1)
    dq = d % (q - 1)  # d mod (q - 1)
    q_inv = mod_inverse(q, p)  # q^(-1) mod p
    
    # Return public key (e, n), private key (d, n), and CRT values (p, q, dp, dq, q_inv)
    return (e, n), (d, n), (p, q, dp, dq, q_inv)

# Function to encrypt a message using RSA
def encrypt(message, public_key):
    e, n = public_key
    # Convert message to integer and encrypt using c = m^e mod n
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Function to decrypt a message using CRT optimization
def decrypt_crt(encrypted_message, private_key, crt_values):
    d, n = private_key
    p, q, dp, dq, q_inv = crt_values
    
    decrypted_message = []
    for char in encrypted_message:
        # Step 1: Compute m1 = c^dp mod p and m2 = c^dq mod q
        m1 = pow(char, dp, p)
        m2 = pow(char, dq, q)
        
        # Step 2: Combine results using CRT: m = m2 + q * ((m1 - m2) * q_inv mod p)
        h = (q_inv * (m1 - m2)) % p
        m = m2 + h * q
        
        # Convert the integer result back to a character
        decrypted_message.append(chr(m))
    
    return ''.join(decrypted_message)

# Example usage
public_key, private_key, crt_values = generate_keys()
message = "HELLO"
print(f"Original message: {message}")

# Encrypt the message
encrypted_message = encrypt(message, public_key)
print(f"Encrypted message: {encrypted_message}")

# Decrypt the message using CRT optimization
decrypted_message = decrypt_crt(encrypted_message, private_key, crt_values)
print(f"Decrypted message (using CRT): {decrypted_message}")
