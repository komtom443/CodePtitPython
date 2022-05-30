import math
A = input().split()
dem = 0
A[0],A[1] = int(A[0]),int(A[1])
for i in range(10**(A[1]-1),10**A[1]-1):
    if(math.gcd(A[0],i) == 1):
        print(i,end=" ")
        dem += 1
        if(dem == 10):
            print()
            dem = 0