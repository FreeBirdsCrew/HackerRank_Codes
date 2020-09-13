"""
Formally, given a wall of infinite height, initially unpainted. There occur N operations, and in ith operation, 
the wall is painted upto height Hi with color Ci. Suppose in jth operation (j>i) wall is painted upto height Hj with 
color Cj such that Hj >= Hi, the Cith color on the wall is hidden. At the end of N operations, you have to find the number 
of distinct colors(>=1) visible on the wall.

Help him find out the number of distinct colors on the wall.
"""
t = int(input())
for _ in range(t):
    n,y = map(int,input().split())
    a = [int(y) for y in input().split()]
    b = [int(y) for y in input().split()]
    m = a[-1]
    ans = []
    ans.append(b[-1])
    for i in range(n-2,-1,-1):
        if a[i] > m:
            m = a[i]
            ans.append(b[i])
    print(len(set(ans)))    