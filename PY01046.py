def towel(N,A,B,C):
    if N == 1:
        print(A,"->",C)
        return
    towel(N-1,A,C,B)
    towel(1,A,B,C)
    towel(N-1,B,A,C)
def solution():
    A = int(input())
    towel(A,'A','B','C')
solution()