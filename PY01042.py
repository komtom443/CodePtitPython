def solution():
    A=input()
    for i in A:
        if(ord(i) < ord('0') or ord(i) > ord('3')):
            print("NO")
            return
    print("YES")
for i in range(0,int(input())):solution()