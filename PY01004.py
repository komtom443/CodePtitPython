import math
def primeCheck(a):
    if(a < 2):
        return 0
    else:
        for i in range(2, a - 1):
            if(a % i == 0):
                return 0
        return 1
def solution():
    N = int(input())
    K = 1
    for i in range(1, N - 1):
        if(math.gcd(N,i) == 1):
            K += 1
    if(primeCheck(K) == 1):
        print("YES")
    else:
        print("NO")
for i in range(int(input())):
    solution()