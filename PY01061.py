def primeCheck(A):
    if(A < 2):
        return 0
    for i in range(2,A-1):
        if A % i == 0:
            return 0
    return 1
def solution():
    A = input()
    if primeCheck(int(A[0:3]))==1 and primeCheck(int(A[len(A)-3:len(A)]))==1:
        print("YES")
        return
    print("NO")
for i in range(0,int(input())):solution()