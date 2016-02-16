__author__ = 'Daniel'
import subprocess


print('Type quit to quit.')
while True:
    file = input('File to run: ')
    if file == 'quit':
        quit()
    subprocess.call(file, shell=True)