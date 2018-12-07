list=[[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
s=[]
for i in range(0,len(list)):
    s.append(sum(list[i]))
print(s)
s.sort()
print(s[len(s)-1])