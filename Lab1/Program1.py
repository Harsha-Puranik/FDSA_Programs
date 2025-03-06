a = [1, 2, 3, 4, 5]
min = a[0]
max = a[0]
for i in range(0, len(a)):
    if(min < a[i]):
        min = a[i]
    elif(max > a[i]):
        max = a[i]
print(min)
print(max)
