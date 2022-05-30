def solution():
    a = input()
    for i in range(0,len(a),2):
        dem = int(a[i+1])
        while dem > 0:
            print(a[i],end="")
            dem -=1
    print()
for i in range(0,int(input())): solution()