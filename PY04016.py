
from datetime import datetime as dt
class KhachHang:
    def __init__(self,id,name,room,startStr,endStr,price):
        self.id = str.format("KH%02d" % int(id))
        self.name = name
        self.room = room
        self.startDate = dt.strptime(startStr,"%d/%m/%Y")
        self.endDate = dt.strptime(endStr,"%d/%m/%Y")
        self.total = self.dateCount() * self.pricePerDay() + price
    def dateCount(self):
        return (self.endDate - self.startDate).days + 1
    def pricePerDay(self):
        tmp = self.room[0:1]
        if tmp == "1":
            return 25
        if tmp == "2":
            return 34
        if tmp == "3":
            return 50
        return 80
    def out(self):
        print(self.id,self.name,self.room,self.dateCount(),self.total)
        return
def mySort(A):
    return A.total
T = int(input())
A = list()
for i in range(0,T):
    A.append(KhachHang(i+1,input().rstrip(),input().rstrip(),input().rstrip(),input().rstrip(),int(input())))
A.sort(key = mySort,reverse=True)
for i in A:
    i.out()
