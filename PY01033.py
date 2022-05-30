import math
def solution():
    A,B =[int(i) for i in input().split()]
    for i in range(A,B-1):
        for j in range(i+1,B):
            for k in range(j+1,B+1):
                if math.gcd(i,j)==1 and math.gcd(i,k)==1 and math.gcd(j,k)==1:
                    print("(",end="")
                    print(i,j,sep=", ",end=", ")
                    print(k,")",sep="")
solution()