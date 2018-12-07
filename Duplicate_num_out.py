list=[1, 21,-4, 103, 21, 4, 1]
l=len(list)
dup=[]
for i in range(0,l):
    for j in range(i+1,l):
        if(int(list[i])==int(list[j])):
            dup.append(list[i])
print(dup)
