#SimranjeetSingh - FreeBirds Crew
import math
def sockMerchant(n, ar):
    
    dic={}
    for i in ar:
        dic[i] = ar.count(i)
    total = sum([math.floor(count/2) for count in  dic.values()])
    return total


print(sockMerchant(9,[10,20,20,10,10,30,50,10,20]))

