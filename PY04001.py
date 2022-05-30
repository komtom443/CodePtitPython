import math
class Point:
    def __init__(self,X,Y):
        self.x = X
        self.y = Y
    def distance(self, B):
        tmp = math.sqrt((self.x- B.x)**2 +(self.y- B.y)**2)
        print(tmp)
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1