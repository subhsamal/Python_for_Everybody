#A program to print the word with maximum occurances in a program.
#input words.txt file and parse each and every word. print the word with maximum number count along with the count.

file_name = input ("Enter the file name to be parsed: ")
if len(file_name) == 0:
    file_name = 'words.txt'
fhandle = open(file_name)
text = fhandle.read()
#print (text)
#print ("\n")
#print (type (text))
text = text.strip()
words = text.split()
#print (words)
#print (type(words))

count = dict ()
for word in words:
    count[word] = count.get(word, 0) + 1


maxCount = None
maxWord = None
for word, count in count.items():
    if maxCount == None or count > maxCount:
        maxCount = count
        maxWord = word
print (maxCount, maxWord)
