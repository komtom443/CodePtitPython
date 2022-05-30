def solution():
    dem = 1
    for i in input():
        tmp = int(i)
        if(dem * tmp != 0):
            dem *= tmp
    print(dem)
for i in range(0,int(input())):solution()