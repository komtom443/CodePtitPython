def solution():
    A = int(input())
    if(A % 7==0):
        print(A)
        return
    for i in range(0,1000):
        A = A + int(str(A)[::-1])
        if(A % 7==0):
            print(A)
            return
    print(-1)    
for i in range(0,int(input())):solution()