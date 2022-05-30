from datetime import datetime as dt
class Player:
    def __init__(self,ten,home,endTime):
        self.id = ""
        self.name = ten
        self.home = home
        for i in home.split():
            self.id += i[0]
        for i in ten.split():
            self.id += i[0]
        self.totalTime = (dt.strptime(endTime,"%H:%M")-dt.strptime("6:00","%H:%M")).seconds / 3600
        self.totalTime = 120 / self.totalTime
    def __str__(self):
        return str.format("%s %s %s %s Km/h" % (self.id, self.name, self.home,  round(self.totalTime)))
def mySort(A):
    return A.totalTime
T,A = int(input()),list()
for i in range(0,T):
    A.append(Player(input(),input(),input()))
A.sort(key = mySort,reverse=True)
for i in A:
    print(i)


