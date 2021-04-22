#A power set is the set containing all the subsets of the given set.
#Eg. s - {1,2} -> P(s) {{},{1},{2},{1,2}}
from functools import reduce
data = {1,2,3}
f = lambda l : reduce(lambda z,x:z+[y+ [x] for y in z], l , [[]])
print(f(data))
