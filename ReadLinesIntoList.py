f = 'myfile.txt'
lines = [lines.strip() for line in open(f)]
print(lines)

'''
open(filename) open the file.
list comprehension help to remove all leading and trailing white-spaces from each line.
'''
