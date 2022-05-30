class KhachHang:
    def __init__(self,id,name,a,b):
        self.id = str(f"KH%02d" % id)
        self.name = name
        self.price = b - a
        self.totalPrice = round(self.priceCount())
    def priceCount(self):
        if self.price > 100:
            tmp = ((int(self.price) - 100) * 200 + 12500)
            return tmp + tmp * 0.05
        if self.price > 50:
            tmp = (int(self.price) % 50 * 150 + 5000)
            return tmp + tmp * 0.03
        tmp = int(self.price) * 100
        return tmp + tmp *0.02
    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.totalPrice}"
def mySort(A):
    return A.totalPrice
if __name__ == "__main__":
    T = int(input()) + 1
    A = list()
    for i in range(1,T):
        A.append(KhachHang(i,input(),int(input()),int(input())))
    A.sort(key = mySort,reverse=True)
    for i in A:
        print(i)
    