a = [10,20,30,40,50]
largest = a[0]
smallest = a[0]
for i in range (0,len(a)):
    if (largest < a[i]):
        largest = a[i]
    elif(smallest > a[i]):
        smallest = a[i]
print(largest)
print(smallest)
min =a.remove(largest)
max = a.remove(smallest)
arr1 = a[0]
arr2 = a[0]
for j in range(0,len(a)):
    if (arr1 < a[j]):
        arr1 = a[j]
    elif (arr2 > a[j]):
        arr2 = a[j]
print(arr1)
print(arr2)
