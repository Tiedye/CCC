__author__ = 'Daniel'


file = open('2008/s1/s1.3.in')
lines = file.readlines()

name = ''
temp = 201
for city in lines:
    # read the city info and if its colder set that city to the coldest city
    tokens = city.split()
    if int(tokens[1]) < temp:
        name = tokens[0]
        temp = int(tokens[1])

print(name)