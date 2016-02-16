__author__ = 'Daniel'


roman_mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'A2': 100, 'B2': 500, 'M': 1000}

file = open('2012/S2/s2.1.in')
token_input = list(reversed(file.readline().strip()))
last_roman_value = 0
aromatic_sum = 0
for i in range(0, len(token_input), 2):
    roman_value = roman_mapping[token_input[i]]
    arabic_value = int(token_input[i+1])
    if roman_value < last_roman_value:
        aromatic_sum -= roman_value*arabic_value
    else:
        aromatic_sum += roman_value*arabic_value
    last_roman_value = roman_value
print(aromatic_sum)