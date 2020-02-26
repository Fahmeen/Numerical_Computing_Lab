def avg(arr):
Sum=0
for i in range(0, len(arr)):
   Sum=Sum+arr[i]
average=Sum/len(arr)
return float(average)

a=[]
for j in range(0, 5, 1):
    a.append(int(input('Enter an integer value:')))
    
print(avg(a))
