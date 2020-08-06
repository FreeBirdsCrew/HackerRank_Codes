def addStrings(num1: str, num2: str) -> str:
    n1=len(num1)
    n2=len(num2)
    carry=0
    x=0
    sum=''
    i=n1-1
    j=n2-1
    while(i>=0 and j>=0):
        x=int(num1[i])+ int(num2[j])+carry
        if(x>9):
            sum=str(x%10) + sum
            carry=1
        else:
            carry=0
            sum= str(x) + sum
        i-=1
        j-=1
    if(i>=0):
        while(i>=0):
            x=int(num1[i]) + carry
            if(x>9):
                sum =str(x%10) + sum
                carry=1
            else:
                carry=0
                sum =str(x) + sum
            i-=1
    if(j>=0):
        while(j>=0):
            x=int(num2[j]) + carry
            if(x>9):
                sum =str(x%10) + sum
                carry=1
            else:
                carry=0
                sum =str(x) + sum
            j-=1
    if(carry==1):
        sum= str(carry)+sum
    return sum


print(addStrings('2321','3'))
