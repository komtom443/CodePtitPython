def check(A,B):
    for i in range(1,B+1):
        if(A[i] <= A[i-1]):
            return False
    for i in range(B+1,len(A)):
        if(A[i]>= A[i-1]):
            return False
    return True
def solution():
    A= input()
    if(len(A) < 3):
        print("NO")
        return
    for i in range(0,len(A)):
        if(check(A,i)==True):
            print("YES")
            return
    print("NO")
for i in range(0,int(input())):solution()