from functools import reduce
n = 5
factorial = reduce(lambda x,y : x*y, range(1,n+1))
print(factorial)

'''
Range can Create Range of Numbers from 1 to n+1
reduce function can multiples all the number together.
'''
