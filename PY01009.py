a = input()
dem = len(a)
count1 = 0
count2 = 0
for i in range(0,dem):
    if(a[i] >= 'a' and a[i] <= 'z'):
        count1 += 1
    if(a[i] >= 'A' and a[i] <= 'Z'):
        count2 += 1
if(count1 >= count2):
    print(a.lower())
else:
    print(a.upper())