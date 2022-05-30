import math
def primeCheck(A):
    if(A < 2):
        return 0
    for i in range(2,A-1):
        if(A % i == 0):
            return 0
    return 1
def solution():
    dem = 0
    inputStr = input().split()
    for i in list(str(math.gcd(int(inputStr[0]),int(inputStr[1])))):
        dem += int(i)
    if(primeCheck(dem)):
        print("YES")
        return
    print("NO")
for i in range(0,int(input())): solution()

    