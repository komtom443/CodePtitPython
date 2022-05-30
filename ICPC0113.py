import math
A = [13]
index = 13
def isPrime(A):
    if A < 2:
        return 0
    for i in range(2,int(math.sqrt(A)+1)):
        if A % i == 0:
            return 0
    return 1
def check(A):
    tmp1,tmp2 = str(A),str(A)[::-1]
    if tmp1 == tmp2:
        return 0
    if A > int(tmp2):
        return 0
    if isPrime(A) == 1:
        return isPrime(int(tmp2))
    return 0

for i in range(0,int(input())):
    tmp = int(input())
    if tmp > index:
        for j in range(index+1,tmp):
            if check(j) == 1:
                A.append(j)
        index = A[len(A)-1]
    for j in A:
        if j >= tmp:
            break
        if int(str(j)[::-1]) < tmp:
            print(j,int(str(j)[::-1]),sep="  ",end="  ")
    print()