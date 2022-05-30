def solution():
    A = input()
    dem,pre = 1,A[0]
    for i in range(1,len(A)):
        if(A[i]==pre):
            dem+=1
        else:
            print(dem,pre,sep="",end="")
            pre = A[i]
            dem = 1
    print(dem,pre,sep="")
for i in range(0,int(input())):solution()