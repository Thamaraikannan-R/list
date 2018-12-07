list1=[1,4,5,6,7,8]
list2=[9,8,7,6,5,5]
print("list1:",list1)
print("list2:",list2)
list3=[]
list4=[]
list5=[]
for i in range(0,len(list1)):
    for j in range(0,len(list2)):
        if (list1[i]==list2[j]):
            list3.append(list1[i])
for i in list3:
    if i not in list4:
        list4.append(i)
print("common elements are:",list4)
list1.extend(list2)
for i in list1:
    if i not in list5:
        list5.append(i)
print("clone List:",list5)

