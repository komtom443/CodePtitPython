def solution():
    inputNum = input()
    i = len(inputNum) - 1
    inputNum = list(inputNum)
    while(i > 0):
        if(int(inputNum[i]) >= 5):
            inputNum[i-1] = str(int(inputNum[i-1])+1)
        inputNum[i] = "0"
        i -= 1
    for i in inputNum:
        print(i,end="")
for i in range(int(input())):
    solution()
    print()