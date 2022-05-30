A = input().lower()
if(len(A) >=3 and A[len(A)-3:len(A)]==".py"):
    print("yes")
else:
    print("no")
