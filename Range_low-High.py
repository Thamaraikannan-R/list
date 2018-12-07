arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
low=20
high=20
l=len(arr)
min=[]
max=[]
out=[]
for i in range(0,l):
    if(int(arr[i])<low):
        min.append(arr[i])
    if(arr[i]==high):
        max.append(arr[i])
if low==high:
    c=0
else:
    min.append(low)
for j in range(0,l):
    if (int(arr[j]) >high):
        max.append(arr[j])
min.extend(max)
print(min)


