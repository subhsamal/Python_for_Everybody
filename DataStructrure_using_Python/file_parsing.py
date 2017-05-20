
#our goal here is is simply to read through a file 'mbox-short.txt' and print out the contents of a file, all in upper case.

file_name = input("Enter the filename to be parsed.")
fhand = open(file_name)
#fhand.read()
for line in fhand:
    line = line.rstrip().upper()
    print (line)
