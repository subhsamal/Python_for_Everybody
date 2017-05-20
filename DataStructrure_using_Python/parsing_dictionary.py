#Using dictionary in Python.
#Count the number of repetition of words in a list using a dictionary.
#This also can be done using get()


count = dict ()
names = ['sumu', 'rosu', 'maku', 'bro', 'sumu', 'rosu', 'sumu']

for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[name] = count[name]+1
print (count)                                                
