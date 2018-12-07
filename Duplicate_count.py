x=[]
y=[]
l=int(input("How many element want to add:"))
for i in range(0,l):
    x.append(input("enter the number to be add:"))
m=int(input("how many numbers want to search:"))
for j in range(0,m):
    y.append(input("enter the number to be search:"))
for k in range(0,len(y)):
    count=0
    for n in range(0,len(x)):
        if y[k]==x[n]:
            count=count+1
    print("number",y[k],"is",count,"times repeated")