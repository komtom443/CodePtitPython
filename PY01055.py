def solution():
    A = input()
    if(A[0]==A[1]or len(A) % 2 == 0):
        print("NO")
        return
    for i in range(0,len(A),2):
        if(A[i] != A[0]):
            print("NO")
            return
    print("YES")
for i in range(0,int(input())):solution()