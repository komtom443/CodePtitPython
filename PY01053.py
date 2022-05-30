def solution():
    dem = 0
    for i in input():
        dem += int(i)
    if dem % 3 == 0:
        print("YES")
        return
    print("NO")
for i in range(0,int(input())):solution()