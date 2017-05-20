#This program is to print top 10 words in a file.

count = dict()

name = input("Enter the file name: ")
if len(name)==0:
    name = 'Romeo.txt'
fhand = open(name)
for line in fhand:                        #going through the file line by line
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0)+1  #count the words in the list using a dictionary
#print (count)

lst = list()
for key, val in count.items():               #item() method is used in dictionary to crete a pair of key and value
    lst.append((val, key))                   #Append (val, key) pair to the list, so that we can sort list by value
#print (lst)


lst.sort(reverse=True)                     #sort the list from asccending to descending

for val, key in lst[:10]:
    print (key,val)
