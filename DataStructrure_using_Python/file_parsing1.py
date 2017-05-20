file_name = input ("Please enter the file name ")
if len(file_name) == 0:
    file_name = 'mbox-short.txt'
fhand = open(file_name)
for line in fhand:
    if line.startswith('From '):
        line = line.rstrip()
        list1= line.split()
        if list1[1] == 'stephen.marquard@uct.ac.za':
            print (list1[2])
