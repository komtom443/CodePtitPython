def solution(A):
    Ans = ""
    i = 0
    while i < len(A):
        tmp = ''
        while(ord(A[i]) >= ord('0') and ord(A[i]) <= ord('9')):
            tmp += A[i]
            i += 1
            if(i >= len(A)):
                break
        if(tmp != ''):
            if Ans == "":
                Ans = int(tmp)
            Ans = min(Ans,int(tmp))
        i += 1
    print(Ans)
for i in range(0,int(input())):
    solution(input())