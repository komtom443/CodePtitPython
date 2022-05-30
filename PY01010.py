def solution():
    strIn = input()
    count = len(strIn)
    if(int(strIn[0:2]) == int(strIn[count - 2:count])):
        print("YES")
        return
    print("NO")
for i in range(0,int(input())):solution()