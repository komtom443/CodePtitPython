
def base_convert(i, b):
    result = []
    while i > 0:
            result.insert(0, i % b)
            i = i // b
    tmp = ""
    for i in result:
        tmp += str(i)
    return tmp

def solution(A,B):
    if A == 2:
        print(B)
        return
    B = int(B,2)
    if A == 8 or A == 4:
        print(base_convert(B,A))
        return
    if A == 16:
        print(str(hex(B)).upper()[2::])
        return
for i in range(0,int(input())):
    solution(int(input()),input())