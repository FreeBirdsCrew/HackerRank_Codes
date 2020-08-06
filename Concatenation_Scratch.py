def addStrings(self, num1: str, num2: str) -> str:
    m = max(len(num1),len(num2))
    ret = ''
    c = 0
    for i in range (-1,-(m+1),-1) :
        x = int(num1[i] if i >= -len(num1) else 0) + int(num2[i] if i >= -len(num2) else 0) + c
        d = x%10
        c = x//10
        ret += (str(d))
    if c > 0 : ret += (str(c))

    return ret[::-1]

print("123","10")
