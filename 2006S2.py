__author__ = 'Daniel'
import string


file = open('2006/s2/s2.1.in')

plaintext = file.readline().strip()
plain_ciphered = file.readline().strip()

char_map = {c: '.' for c in string.ascii_uppercase}
char_map[' '] = '.'
for a, b in zip(plaintext, plain_ciphered):
    char_map[b] = a

ciphertext = file.readline().strip()
print(ciphertext.translate(str.maketrans(char_map)))