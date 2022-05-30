def check(A):
    A = str(A)
    N = len(A)
    if(N % 2 == 1):
        return
    if(A!=A[::-1]):
        return
    for i in A:
        if(int(i) % 2 == 1):
            return
    print(A,end=" ")
def solution():
    A = int(input())
    for i in range(22,A,2):
        check(i)
    print()
for i in range(0,int(input())):solution()