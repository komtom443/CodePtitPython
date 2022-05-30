from math import *
class PhanSo:
    def __init__(self,A):
        tmp = int(gcd(int(A[0]),int(A[1])))
        self.x,self.y = int(int(A[0]) / tmp),int(int(A[1])/ tmp)
    def __str__(self):
        if self.x == 0:
            return "0"
        if self.y == 1:
            return str(self.x)
        return f"{self.x}/{self.y}"
print(PhanSo(' '.join(input().split()).split()))
    