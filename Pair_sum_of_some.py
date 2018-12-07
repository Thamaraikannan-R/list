arr1 = [-1, -2, 4, -6, 5, 7]
arr2 = [6, 3, 4, 0]
n=8
for i in range(0,len(arr1)):
    for j in range(0,len(arr2)):
        if(int(arr1[i])+int(arr2[j])==n):
            print("SUM of 8 - ",arr1[i],arr2[j])
        elif (int(arr1[i])+int(arr2[j])==9):
            print("SUM of 9 -",arr1[i],arr2[j])