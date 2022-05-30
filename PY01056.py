def solution():
    A=input()
    dem = 0
    for i in range(0,len(A)):
        if(int(A[i]) % 2 != i % 2):
            print("NO")
            return
        dem += int(A[i])
    if(dem < 2):
        print("NO")
        return
    for i in range(2,dem):
        if dem % i == 0:
            print("NO")
            return
    print("YES")
for i in range(0,int(input())):solution()