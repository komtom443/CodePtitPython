def check(A):
    if(A < 2):
        return
    for i in range(2,A):
        if A % i == 0:
            return 0
    return 1
def fcheck(A):
    if(A == 2 or A == 3 or A == 5 or A == 7):
        return 1
    return 0
def solution():
    A = input()
    for i in range(0,len(A)):
        if(check(i) == 1 and fcheck(int(A[i])) == 0):
            print("NO")
            return
        if(check(i) == 0 and fcheck(int(A[i])) == 1):
            print("NO")
            return
    print("YES")
for i in range(0,int(input())):solution()