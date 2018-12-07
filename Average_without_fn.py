list=[15, 9, 55, 41, 35, 20, 62, 49]
l=len(list)
sum=0
for i in range(0,l):
    sum=sum+int(list[i])
print("Average of the list =",sum/l)