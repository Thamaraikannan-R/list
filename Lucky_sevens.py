list=[1,0,1,5,4,7,6,5,0 ,2]
l=len(list)
count=0
for i in range(2,l):
    if(list[i]+list[i-1]+list[i-2]==7):
       count=1
if count==1:
    print("true")
else:
    print("flase")