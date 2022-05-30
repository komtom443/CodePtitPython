T = int(input())
tmp = input().split()
A,B=[],[]
for i in tmp:
    A.append(int(i))
for i in A:
    if len(B) == 0:
        B.append(i)
    else:
        if (B[len(B)-1] + i) % 2 == 0:
            B.pop()
        else:
            B.append(i)
print(len(B))
        


             