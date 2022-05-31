N,Count = int(input()),0
A = [int(i) for i in input().split()]
for i in range(1,N):
    if A[i] + A[i-1] == 1:
        Count += 1
print(Count)
