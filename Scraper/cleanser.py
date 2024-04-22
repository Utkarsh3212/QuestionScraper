import re

arr=[]

with open('pLinks.txt','r') as f:
    for line in f:
        arr.append(line)

def pattern_remover(array,pattern):
    new_array=[]
    for i in arr:
        if pattern not in i:
            new_array.append(i)
        else:
            print("removed: "+ i)
    return new_array

arr=pattern_remover(arr,"/solution")
arr=pattern_remover(arr,"/accounts")

arr=list(set(arr))

with open('properPLinks.txt','w') as f:
    for i in arr:
        f.write(i)


