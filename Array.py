#Array is a collection of data items of same type

from array import *
a1=array('i',[1,2,3,4,5,6])

type(a1) 
print(a1)
print(type(a1))

#print all the elements of a1.
for x in a1:
    print(x)
#print all the elements of a1
for i in range(3):
    print(a1[i],end=" ")

#print all the elements of a1
while (i<len(a1)):
    print(a1[i],end=" ")
    i+=1
# adds 20 in a1
a1.append(20)

#count occurance of 20 in a1
a1.count(20)
a1.count(2)

