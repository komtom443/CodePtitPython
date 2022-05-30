def solution():
    N = input()
    dem = len(N)
    for i in range(1,dem):
        if(N[i-1]>N[i]):
            print("NO")
            return
    print("YES")
for i in range(0,int(input())): solution()