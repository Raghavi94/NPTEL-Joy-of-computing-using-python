# NPTEL-The-Joy-of-computing-using-python

## This repo has programming assignment solutions of python nptel course

WEEK 3:

arr=input().split()
a=[]
b=[]
for i in range(len(arr)):
  if arr[i].endswith("4"):
    a.append(arr[i])
  else:
    b.append(arr[i])
    
    
listToStr = ' '.join([str(elem) for elem in b])
print(listToStr)
   
