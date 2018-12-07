list=[1, 2, 3, 4, 5, 6]
l=int(len(list))
print(l)
output=[]
n=int(input("enter the n postiton to right rotation:"))
for i in range(l-n,l):
    output.append(list[i])
for j in range(0,l-n):
    output.append(list[j])
print(output)