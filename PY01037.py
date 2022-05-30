def check(A):
    dem = 1
    for i in range(1,int(A/2+1)):
        if(A % i == 0):
            dem += 1
    return dem
def solution():
    N = int(input())
    max = 0
    ans = 0
    for i in range(1,N):
        tmp = check(i)
        if tmp > max:
            max = tmp
    if(N %2 ==1):
        N += 1
    while True:
        tmp = check(N)
        if tmp > max:
            print(N)
            return
        N += 2
for i in range(0,int(input())):solution()