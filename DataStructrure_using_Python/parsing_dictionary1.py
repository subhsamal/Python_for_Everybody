#Parsing using dictionary. Count the number of each word in a list using get ()
# Get() takes two parameters. First parameter is the key name which is to be searched and second parameter is the value to give back if
# first parameter does not exist.

count = dict()
names = ['sumu', 'rosu', 'bro', 'maku', 'sumu', 'rosu', 'sumu']

for name in names:
    count[name] = count.get(name, 0) + 1

print (count)
