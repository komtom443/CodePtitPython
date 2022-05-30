from decimal import *
class SoPhuc:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def plus(self,A):
        return SoPhuc(self.x + A.x,self.y + A.y)
    def mul(self,A):
        a = self.x * A.x - self.y * A.y
        b = self.x * A.y + self.y * A.x
        return SoPhuc(a,b)
    def __str__(self):
        if self.y < 0:
            return str(f"%d - %di" % (self.x,self.y * (-1) ))
        return str(f"%d + %di" % (self.x,self.y))
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = SoPhuc(Decimal(arr[0]), Decimal(arr[1]))
        p2 = SoPhuc(Decimal(arr[2]), Decimal(arr[3]))
        p3 = p1.plus(p2)
        print(p3.mul(p1),p3.mul(p3),sep=", ")
        t -= 1