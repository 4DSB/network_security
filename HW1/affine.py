# This is a python implementation of a message being encrypted and decrypted 
# using the affine cipher
# Python v3.X
# Author: Anurag Mittal
# Purpose: Submission for Homework 1 for EE209 - Network Security Class

def encrypt_text(self, a, b, plain_text):
    self.cipher = "";
    for letter in plain_text:
        if letter == ' ':
            


print('Affine Cypher has the following form:')
print('C = E([a, b], p) = (ap + b) mod 26')

a = input('Please enter the value of a: ')
b = input('Please enter the value of b: ')

encrypt = raw_input('Do you want to encrypt a message? (yes/no): ').lower()
if (encrypt == 'no' or encrypt == 'n'):
    decrypt = raw_input('Do you want to decrypt a message? (yes/no): ').lower()
    cipher_text = raw_input('Please enter a message to decrypt: ')
    plain_text = decrypt_text(self, a, b, cipher_text)

else:
    plain_text = raw_input('Please enter a message to encrypt: ')
    cipher_text = encrypt_text(self, a, b, plain_text)

print('Encrypted message is: ' + cipher_text)
print('Decrypted message is:' + plain_text)