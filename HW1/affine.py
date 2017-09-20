# This is a python implementation of a message being encrypted and decrypted 
# using the affine cipher
# Python v3.X
# Author: Anurag Mittal
# Purpose: Submission for Homework 1 for EE209 - Network Security Class

def encrypt_text(a, b, plain_text):
    cipher = "";
    for letter in plain_text:
        if letter != ' ':
            cipher = cipher + (chr)((((a * (ord(letter) - ord('A'))) + b) % 26) + ord('A'))
        else:
            cipher += letter
    return cipher

def decrypt_text(a, b, cipher):
    plainText = ""
    a_inv = 0
    flag = 0

    # Find a^-1 (the multiplicative inverse of a in the group of integers modulo m.)
    for i in range(26):
        flag = (a * i) % 26
        if flag == 1:
            a_inv = i
            break
    
    for letter in cipher:
        if letter != ' ':
            plainText = plainText + (chr)((a_inv * (ord(letter) + ord('A') - b) % 26) + ord('A'))
        else:
            plainText += letter
    return plainText

print('Affine Cypher has the following form:')
print('C = E([a, b], p) = (ap + b) mod 26')

a = input('Please enter the value of a: ')
b = input('Please enter the value of b: ')

encrypt = raw_input('Do you want to encrypt a message? (yes/no): ').lower()
if (encrypt == 'no' or encrypt == 'n'):
    decrypt = raw_input('Do you want to decrypt a message? (yes/no): ').lower()
    cipher_text = raw_input('Please enter a message to decrypt: ').upper()
    plain_text = decrypt_text(a, b, cipher_text)

else:
    plain_text = raw_input('Please enter a message to encrypt: ').upper()
    cipher_text = encrypt_text(a, b, plain_text)

print('Encrypted message is: ' + cipher_text)
print('Decrypted message is: ' + plain_text)