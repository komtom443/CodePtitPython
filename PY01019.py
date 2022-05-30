
def solution():
    A = input()
    B = A[::-1]
    for i in range(1,len(A)):
        if (abs(ord(A[i])-ord(A[i-1]))!=abs(ord(B[i])-ord(B[i-1]))):
            print("NO")
            return
    print("YES")
for i in range(0,int(input())):solution()