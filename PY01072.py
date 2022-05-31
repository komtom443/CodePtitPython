from itertools import combinations
tmp,tmp1 = [int(i) for i in input().split()],[int(i) for i in input().split()]
N,K,A = tmp[0],tmp[1],dict()
for i in tmp1:
    A[i] = 1
A = list(A.keys())
A.sort()
for i in list(combinations(A,K)):
    for j in list(i):
        print(j,end=" ")
    print()