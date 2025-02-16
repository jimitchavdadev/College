import random
import hashlib
from math import gcd

# Generate a prime number p and a generator g
def generate_parameters():
    p = 23  # A small prime number
    g = 5   # A primitive root modulo p
    return p, g

# Generate private and public keys
def generate_keys(p, g):
    x = random.randint(1, p - 2)  # Private key
    y = pow(g, x, p)              # Public key
    return x, y

# Sign a message
def sign_message(message, x, p, g):
    while True:
        k = random.randint(1, p - 2)  # Random integer
        
        if gcd(k, p - 1) != 1:  # Ensure k is coprime to p - 1
            continue
        
        r = pow(g, k, p) % p          # r = (g^k mod p)

        if r == 0:  # r must not be zero
            continue

        k_inv = pow(k, -1, p - 1)     # Modular inverse of k
        hash_message = int(hashlib.sha256(message.encode()).hexdigest(), 16)
        s = (k_inv * (hash_message + x * r)) % (p - 1)  # s = k_inv * (H(m) + x * r) mod (p - 1)

        if s != 0:  # s must not be zero
            return r, s

# Verify a signature
def verify_signature(message, r, s, y, p, g):
    if r < 1 or r >= p or s < 1 or s >= (p - 1):
        return False  # r and s must be in valid ranges

    hash_message = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    w = pow(s, -1, p - 1)          # w = s^(-1) mod (p - 1)
    u1 = (hash_message * w) % (p - 1)  # u1 = (H(m) * w) mod (p - 1)
    u2 = (r * w) % (p - 1)          # u2 = (r * w) mod (p - 1)

    v = (pow(g, u1, p) * pow(y, u2, p)) % p  # v = (g^u1 * y^u2 mod p) mod p
    return v == r  # Valid if v == r

# Example usage
p, g = generate_parameters()
x, y = generate_keys(p, g)

message = "This is a secret message."
r, s = sign_message(message, x, p, g)
print(f"Signature: (r={r}, s={s})")

is_valid = verify_signature(message, r, s, y, p, g)
print("Signature is valid." if is_valid else "Signature is invalid.")
