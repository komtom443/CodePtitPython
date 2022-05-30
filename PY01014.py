inputStr = input().split()
check = 0
for i in range(0,int(inputStr[2]) + 1,int(inputStr[1])):
    if(i - int(inputStr[0])>0):
        print(i - int(inputStr[0]),end=" ")
        check = 1
if check == 0: print("-1")