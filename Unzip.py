z = [(1,2),(3,4),(5,6),(7,8)]
#one liner
unzip = lambda z : list(zip(*z))
print(unzip(z))


"""
* operator remove the enclosing data inside the zip z.
zip takes 2 to n iterables as input and create a new iterable.
"""

#Getting the First and Last Element of list
l = [1,2,3,4,5]
frst, *x, last = l
print(frst)
print(x)
print(last)
