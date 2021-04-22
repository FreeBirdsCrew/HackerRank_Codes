fib = lambda n: n if n <= 1 else fib(n-1) + fib(n-2)
"""str(fib(n-1)) + "" + str(fib(n-2))"""
result= fib(10)
print(result)

'''
lambda expression returns 0 if n == 0 and 1 if n == 1
if n>1, lambda retunrs the fib(n-1) + fib(n-2) which is recursive call.
'''
