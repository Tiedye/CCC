__author__ = 'Daniel'


file = open('2010/S2/s2.6.in')

codes = {}
k = float(file.readline())
for i in range(int(k)):
    # read k codes from the first k lines
    character, code = file.readline().split()
    # reads the character into character and the binary code into code
    codes[code] = character
    # puts the code into a dictionary with its character it represents

sequence = file.readline()
# read the binary sequence into a string
substring = ''
# this will hold the bits we're looking at, if we find that these bits match one of the codes, we add that codes
# corresponding character to the end of the decoded string and look at some new bits (clear the substring)
decoded = ''
for bit in sequence:
    # loops through every bit in the sequence
    substring += bit
    if substring in codes:
        decoded += codes[substring]
        substring = ''

print(decoded)