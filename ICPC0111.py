def solution():
    tmp,B = input().split(),[]
    N,d = int(tmp[0]),int(tmp[1])
    A = [int(i) for i in input().split()]
    A.reverse()
    for i in range(0,N):
        B.append(0)
    for i in range(0,N):
        B[(i + d) % N] = A[i]
    for i in range(N-1,-1,-1):
        print(B[i],end=" ")
    print()
for i in range(0,int(input())):
    solution()