list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
set1=set(list1)
set2=set(list2)
print("Missing value in list1:",set2.difference(set1))
print("Additional vaslue in list1:",set1.difference(set2))
print("Missing values in list2:",set1.difference(set2))
print("Additional values in list2:",set2.difference(set1))
