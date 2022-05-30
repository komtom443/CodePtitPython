def solution():
    A = int(input())
    dem = 0
    if(A % 2 == 1):
        for i in range(1,A+1,2):
            dem += 1/i
    else:
        for i in range(2,A+1,2):
            dem += 1/i
    print('%.6f'%dem)
for i in range(0,int(input())):solution()