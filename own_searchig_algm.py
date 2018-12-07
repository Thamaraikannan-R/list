list=[1,4,6,7,8,9,0,12,14,16,24,26,28,29,41,52,64,56,67,86,56,67,678,65]
a=[]
n=int(input("How many elemments want to be search:"))

for k in range(0,n):
    a.append(int(input("Enter the elements:")))
print(a)
for i in range(0,len(list)):
    for j in range(0,len(a)):
        if(a[j]==list[i]):
            print("element ",a[j]," found index of",list.index(list[i]))

for h in a:
    if h not in list:
         print("-1")

