def solution():
    S = input()
    N = input()
    dem = 0
    if(len(N) > len(S)):
        print(0)
        return
    i = 0
    while(i <= len(S)-len(N)):
        if(S[i:i+len(N)]==N):
            dem += 1
            i += len(N)
        else:
            i+=1
    print(dem)
for i in range(0,int(input())):solution()