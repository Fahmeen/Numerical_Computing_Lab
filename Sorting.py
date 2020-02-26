arr=[]
for i in range(0,5)
    num=int(input("Enter a number:"))
    arr.append(int(num))
    
for k in range(0,4):
    max=arr[0]
    location=0
    for j in range(1,5-k):
        if arr[j]>max:
            max=arr[j]
            locatio=j
    temp=arr[j]
    arr[j]=arr[location]
    arr[location]=temp
for num in arr:
    print("\nSorted array:"+str(num))
