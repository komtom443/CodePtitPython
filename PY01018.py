from audioop import reverse


p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    inputStr = input().split()
    if inputStr[0] == "0":
        break
    str = inputStr[1]
    ans = ""
    for i in str:
        ans +=p[(p.find(i)+int(inputStr[0]))%28]
    ans = list(ans)
    ans.reverse()
    for i in ans: print(i,end="")
    print()