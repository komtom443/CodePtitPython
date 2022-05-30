import math
def solution():
    A = input()
    if(math.gcd(int(A),int(A[::-1])) == 1):
        print("YES")
        return
    print("NO")
for i in range(0,int(input())):solution()