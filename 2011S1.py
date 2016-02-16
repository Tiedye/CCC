__author__ = 'Daniel'
from collections import Counter


file = open('2011/s1/s1.1.in')
string = ''
for line in file.readlines():
    string += line.strip().lower()
chars = Counter(string)
del chars[' ']
if 't' not in chars:
    chars['t'] = 0
if 's' not in chars:
    chars['s'] = 0
if chars['t'] > chars['s']:
    print('English')
else:
    print('French')