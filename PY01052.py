def solution():
    A = 0
    for i in input():
        A += int(i)
    if(A < 2):
        print("NO")
        return
    for i in range(2,A):
        if A % i == 0:
            print("NO")
            return
    print("YES")
for i in range(0,int(input())):solution()