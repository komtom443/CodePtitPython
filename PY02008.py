from math import sqrt
def isPrimed(A):
    if A < 2:
        return 0
    for i in range(2,int(sqrt(A))+1):
        if A % i ==0:
            return 0
    return 1
tmp = [int(i) for i in input().split()]
Count,Ans =tmp[0],tmp[1]
tmp = 2
print(Ans,end = " ")
while Count > 0:
    if isPrimed(tmp) == 1:
        Ans += tmp
        print(Ans,end = " ")
        Count -= 1
    tmp += 1
