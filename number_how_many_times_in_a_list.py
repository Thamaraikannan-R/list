list=[8, 6, 8, 10, 8, 20, 10, 8, 8]
x=16
count=0
l=len(list)
for i in range(0,l):
    if(int(list[i])==x):
        count=count+1
print("Number",x,"is",count,"times repeated in a list")