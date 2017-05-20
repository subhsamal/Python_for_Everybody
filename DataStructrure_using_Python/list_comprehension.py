# This program is using list comprehension
#the top 10 word program can be done using list comprehension only in couple of lines.

c = {'a': 10, 'b':20, 'c':30}
print (sorted([(v,k) for k,v in c.items()]))
