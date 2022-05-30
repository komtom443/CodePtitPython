def solution():
    A = input()
    if(A[0] == A[1]):
        print("NO")
        return
    for i in range(0,len(A)):
        if(i % 2 == 0 and A[i] != A[0]):
            print("NO")
            return
        if(i % 2 == 1 and A[i] != A[1]):
            print("NO")
            return
    print("YES")

for i in range(0,int(input())):solution()