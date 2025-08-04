""" "
implement SHA1 in pythn
input to SHA1 = your roll number (22BCP225)
gives output= 160bits
adding, prefix or suffic to your roll number
so that the output contain first three bits as zero
"""

import hashlib


def sha1_with_condition(base_input):
    attempt = 0
    while True:
        # Try suffix (could also try prefix)
        trial_input = base_input + str(attempt)
        # Get SHA-1 hash
        hash_obj = hashlib.sha1(trial_input.encode())
        digest = hash_obj.digest()  # raw 20 bytes (160 bits)
        # Convert to binary string
        bin_hash = bin(int.from_bytes(digest, byteorder="big"))[2:].zfill(160)

        # Check first 3 bits
        if bin_hash.startswith("000"):
            print(f"Modified Input   : {trial_input}")
            print(f"SHA-1 (Hex)      : {hash_obj.hexdigest()}")
            print(f"SHA-1 (Binary)   : {bin_hash}")
            print(f"First 3 bits     : {bin_hash[:3]}")
            break
        attempt += 1


sha1_with_condition("22BCP225")
