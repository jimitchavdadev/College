import random

# Function to find the greatest common divisor (gcd) using the Euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to compute the modular inverse of e mod φ(n) using the Extended Euclidean Algorithm
def mod_inverse(e, phi):
    # Nested function to perform the Extended Euclidean Algorithm
    def egcd(a, b):
        if a == 0:
            return b, 0, 1  # Base case: when a = 0, return gcd(b, 0), and coefficients
        g, x, y = egcd(b % a, a)  # Recursive case
        return g, y - (b // a) * x, x
    
    g, x, y = egcd(e, phi)  # Compute gcd(e, φ) and the coefficients x, y
    if g != 1:
        raise Exception('Modular inverse does not exist')  # e and φ(n) must be coprime
    return x % phi  # Return the positive modular inverse of e

# Function to generate the public and private RSA keys
def generate_keys():
    # Step 1: Choose two large prime numbers p and q (small primes used here for simplicity)
    p = 61
    q = 53
    # Compute n = p * q, which will be used as part of both the public and private keys
    n = p * q
    
    # Step 2: Compute the totient function φ(n) = (p-1) * (q-1)
    phi = (p - 1) * (q - 1)
    
    # Step 3: Choose a random integer e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
    e = random.choice([i for i in range(2, phi) if gcd(i, phi) == 1])
    
    # Step 4: Compute the private exponent d such that (d * e) ≡ 1 (mod φ(n))
    d = mod_inverse(e, phi)
    
    # Return the public key (e, n) and the private key (d, n)
    return (e, n), (d, n)

# Function to encrypt a message using the public key
def encrypt(message, public_key):
    e, n = public_key
    # Convert each character in the message to its ASCII value (integer)
    # Encrypt each character using the formula: c = m^e mod n, where m is the ASCII value
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Function to decrypt an encrypted message using the private key
def decrypt(encrypted_message, private_key):
    d, n = private_key
    # Decrypt each character using the formula: m = c^d mod n, where c is the encrypted value
    # Convert the decrypted value (integer) back to a character (ASCII)
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

# Example usage
public_key, private_key = generate_keys()  # Generate the RSA key pair
message = "HELLO"  # The original message to be encrypted
print(f"Original message: {message}")

# Encrypt the message using the public key
encrypted_message = encrypt(message, public_key)
print(f"Encrypted message: {encrypted_message}")

# Decrypt the message using the private key
decrypted_message = decrypt(encrypted_message, private_key)
print(f"Decrypted message: {decrypted_message}")
