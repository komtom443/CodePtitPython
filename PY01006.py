def solution():
    inputNum = input()
    for i in inputNum:
        if(i != '4' and i != '7'):
            return 0
    return 1
for i in range(int(input())):
    if(solution()):
        print("YES")
    else:
        print("NO")