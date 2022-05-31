def solution(tmp,Ans):
    A,B = tmp[0],tmp[1]
    for i in range(A-1,B):
        print(Ans[i],end = " ")
Ans = [1,1]
tmp = 1
while tmp <= 93:
    Ans.append(Ans[len(Ans)-1]+Ans[len(Ans)-2])
    tmp += 1
for i in range(0,int(input())):
    solution([int(i) for i in input().split()],Ans)
    print()