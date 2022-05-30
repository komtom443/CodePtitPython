def solution():
    A =str("0000"+input())
    A = int(A[len(A)-4:len(A)])
    if(A < 2):
        print("NO")
        return
    for i in range(2,A):
        if A % i == 0:
            print("NO")
            return
    print("YES")
for i in range(0,int(input())):solution()