def solution():
    A = input()
    sum,mul,check =0,1,0
    for i in range(1,len(A),2):
        sum+= int(A[i])
    for i in range(0,len(A),2):
        if int(A[i]) != 0:
            mul *= int(A[i])
            check = 1
    if(check == 0):
        print("0",end =" ")
    else:
        print(mul,end = " ")
    print(sum)
for i in range(0,int(input())):solution()