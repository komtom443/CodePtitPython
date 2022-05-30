class KhachHang:
    def __init__(self,id,name,strInput):
        strInput = strInput.split()
        self.__id = str(f"KH%02d" % id)
        self.__name = self.chuanHoa(name)
        self.__totalPrice = 0
        self.__type = strInput[0]
        self.__amount = int(strInput[2])-int(strInput[1])
        

    def chuanHoa(self,strInput):
        ans = ""
        strInput = " ".join(strInput.rstrip().lstrip().split()).split()
        for i in strInput:
            ans += i.upper()[0]+i.lower()[1:len(i)]+" "
        return ans.rstrip()

    def __str__(self) -> str:
        return self.__id + " " + self.__name
    
    def getTotalPrice(self):
        return self.__totalPrice
def mySort(A):
    return A.getTotalPrice()
A = list()
for i in range(1,int(input())+1):
    A.append(KhachHang(i,input(),input()))
A.sort(key=mySort,reverse=True)
for i in A:
    print(i)
