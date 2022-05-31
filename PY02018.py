def solution():
    N,B = int(input()),dict()
    for i in range(1,N+1):
        B[i] = 0 
    for i in input().split():
        B[int(i)] = 1
    for i in range(1,N+1):
        if B[i] == 0:
            print(i)
            return
    print(N + 1)
solution()