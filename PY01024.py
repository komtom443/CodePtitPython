def solution():
    A = input()
    dem = int(A[0])
    for i in range(1,len(A)):
        if abs(int(A[i])-int(A[i-1])) != 2:
            print("NO")
            return
        dem+=int(A[i])
    if dem % 10 == 0:
        print("YES")
    else:
        print("NO")
for i in range(0,int(input())):solution()