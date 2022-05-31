def solution(N,A,B):
    A.sort()
    B.sort()
    for i in range(0,N):
        if A[i] > B[i]:
            return "NO"
    return "YES"
for i in range(0,int(input())):
    print(solution(int(input()),[int(i) for i in input().split()],[int(i) for i in input().split()]))