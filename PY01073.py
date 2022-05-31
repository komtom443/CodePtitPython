from itertools import permutations
A,B = input(),[]
for i in range(0,len(A)):
    B.append(i)
for i in list(permutations(B)):
    print("".join([A[j] for j in list(i)]))