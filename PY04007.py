def solution():
    tmp = input().split()
    m,n = int(tmp[0]),int(tmp[1])
    A = list()
    for i in range(0,m):
        B = list()
        tmp = input().split()
        for j in tmp:
            B.append(int(j))
        A.append(B)
    for i in A:
        for j in A:
            print(mul(i,j),end = " ")
        print()
def mul(A,B):
    ans = 0
    for i in range(0,len(A)):
        ans += A[i] * B[i]
    return ans
        

for i in range(0,int(input())):
    solution()