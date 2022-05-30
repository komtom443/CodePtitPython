
class Rectangle:
    def __init__(self,A):
        A = A.split()
        self.w,self.h,self.color = int(A[0]),int(A[1]),A[2].upper()[0]+A[2].lower()[1:len(A[2])]
    def __str__(self):
        if self.h > 0 and self.w >0:
            return str(f"{(self.w+self.h) * 2} {self.h * self.w} {self.color}")
        return "INVALID"
print(Rectangle(input()))