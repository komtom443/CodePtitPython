def solution():
    A = int(input())
    if(A == 1):
        print(1)
        return
    print("1 * ",end="")
    if(A==0):
        print("0")
        return
    i,dem = 2,0
    while(1):
        if(i * i > A):
            if(A == i):
                dem += 1
                print(i,"^",dem,sep="")
            if(A !=i):
                if(dem != 0):
                    print(i,"^",dem,sep="",end=" * ")
                print(int(A),"^",1,sep="",)
            return 1
        if(A % i == 0):
            dem += 1
            A = A / i
        else:
            if(dem != 0):
                print(i,"^",dem,sep="",end=" * ")
            i += 1
            dem = 0
for i in range(0,int(input())):
    solution()