word = "wow"
p = bool(word.find(word[::-1])+1)
print(p)

'''
Returns True if the Word is Palindrome.
word[::-1] invert the input word.
word.find(s) find the index of s inside the word return 0 or -1 for True or False.
bool(0) =  Flase and bool(1) = True
'''
