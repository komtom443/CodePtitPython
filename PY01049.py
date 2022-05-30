def solution():
    A = input()
    B = len(A)
    if(B < 2):
        print("NO")
        return
    for i in range(2,B):
        if B % i == 0:
            print("NO")
            return
    p,np = 0,0
    for j in A:
        i = int(j)
        if i == 2 or i == 3 or i == 5 or i == 7:
            p +=1
        else:
            np +=1
    if(p > np):
        print("YES")
    else:
        print("NO")
for i in range(0,int(input())):solution()