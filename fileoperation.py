
f = open('myFile.txt', 'r')

for line in f:
    print (line, end='')

f.close()
'''

f = open('myFile.txt', 'a')

f.write('\nThis sentence will be appended')
f.write('\nPython is Fun!')

f.close()
'''
