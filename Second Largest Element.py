"""
All submissions for this problem are available.Find the length of the longest contiguous segment in an array, 
in which if a given element K is inserted, K becomes the second largest element of that subarray.

Input:
The first line will contain T, number of test cases. Then the test cases follow.
The first line of each test case contains two integers N and K.
The next line contains N space-separated integers Ai denoting the elements of the array.

Output:
Print a single line corresponding to each test case — the length of the largest segment.

"""
T = int(input())


for q in range(T):
    n,m = map(int,input().strip().split())
    arr = list(map(int,input().strip().split()))
    c = 0
    ind = []
    mp = {}
    k = 0
    h = 0
    arr.append(max(arr)+1)
    for i in range(n+1):
        #print(c)
        if arr[i]<=m:
            c+=1
        else:
            if h==0:
                h = 1
                k = i
                c+=1
            else:
                if arr[k]==arr[i]:
                    c+=1
                    k = i
                else:
                    #print(arr[i])
                    ind.append(c)
                    c = max(1,i-k)
                    k = i
    #print(ind)
    if len(ind)==0:
        print(0)
    else:
        print(max(ind))
            
        