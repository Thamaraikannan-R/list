list=[3, 5, 2, -4, 8, 11]
l=len(list)
d=0
m=[]
for i in range(0,l):
    for j in range(i+1,l):
        d=list[i]+list[j]
        if(d==7):
            print("[",list[i],",",list[j],"]")
