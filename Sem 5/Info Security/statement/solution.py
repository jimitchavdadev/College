"""
Design cipher with detailed explanation. Sample as
follows.


a) Write a program to encrypt the plaintext with the
given key. E.g. plaintext GRONSFELD with the
key 1234. Add 1 to G to get H (the letter 1 rank
after G is H in the alphabet), then add 2 to C or
E (the letter 2 ranks after C is E), and so on. Use
smallest letter from plaintext as filler.
b) Encrypt the input words PLAINTEXT= RAG
BABY to obtain CIPHERTEXT = SCJ DDFDZ
"""

# 1.

def encrypt(text, rank):
    length = len(str(rank))
    rank = [int(digit) for digit in str(rank)]

    i = 0
    encrypted_text = ''
    
    for char in text:
        if char.isalpha() and char.isupper():
            char_num = ord(char) - 65
            encrypted_char_num = (char_num + rank[i % length]) % 26
            encrypted_char = chr(encrypted_char_num + 65)
            encrypted_text +=  encrypted_char
        elif char.isalpha() and char.islower():
            char_num = ord(char)  - 97
            encrypted_char_num = (char_num + rank[i % length]) % 26
            encrypted_char = chr(encrypted_char_num + 97)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
        
        i = (i+1)%length
    return encrypted_text

print(encrypt('GRONSFELD',1234))

# 2.

def encrypt(text):
    text_num = 0
    word = 0

    encrypted_text = ""
    for char in text:
        if char == " ":
            word += 1
            text_num = 0
            encrypted_text += char
        else:
            text_num += 1
            if char.isalpha() and char.isupper():
                char_num = ord(char) - 65
                char_text = (char_num + word + text_num) % 26
                encrypted_text += chr(char_text+ 65)
            elif char.isalpha() and char.islower():
                char_num = ord(char) - 97
                char_text = (char_num + word + text_num) % 26
                encrypted_text += chr(char_text+ 97)
            else:
                encrypted_text += char
    return encrypted_text

print(encrypt('RAG BABY'))