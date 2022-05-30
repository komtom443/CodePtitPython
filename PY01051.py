def solution():
    dem = 0
    for i in input():
        dem += int(i)
    if(dem < 10):
        print("NO")
        return
    if(dem == int(str(dem)[::-1])):
        print("YES")
        return
    print("NO")
for i in range(0,int(input())):solution()