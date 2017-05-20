str = 'X-DSPAM-Confidence: 0.8475'
print (str)
pos = str.find(':')
new_str = str[pos+1:]
print (new_str)
