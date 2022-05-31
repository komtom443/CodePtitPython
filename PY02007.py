A = dict()
tmp = 0
while tmp < 10:
    for i in input().split():
        A[int(i) % 42] = 1
        tmp += 1
print(len(A))
