A = [0,0,0,0,0,0,0,0,0,0,0,0]
Count = ['A','B','C']
Ans=[]
def ss(A):
    return len(A)
def tripGen(B,C):
    for i in range(0,3):
        if(B >= 3 and B <= C):
            demA,demB,demC=A[0:B].count('A'),A[0:B].count('B'),A[0:B].count('C')
            if(demA !=0 and demB !=0 and demC !=0  and demB >= demA and demC>=demB):
                tmp = ''.join(str(i)for i in A[0:B])
                if(Ans.count(tmp) == 0):
                    Ans.append(tmp)
        if(B==C):
            return
        A[B] = Count[i]
        tripGen(B+1,C)
C = int(input())
if(C>=3):
    LimNum = int(C /3)+1
    tripGen(0,C)
    Ans.sort()
    Ans.sort(key=ss)
    for i in Ans:
        print(i)