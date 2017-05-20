#Use of Items() method in Dictionary and in Tuple
'''
d = dict()
d['csev'] = 2
d['cwen'] = 2
for (key, value) in d.items():
    print (key, value)
'''
#The above program can be implemented using Tuple and items() method
d = {'csev': 2, 'cwen':2}
#print (d)
tups = d.items()   #this will create tuples out of key value pairs
print (tups)
