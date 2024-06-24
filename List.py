'''
l1=[10,56,'shashank'] 

class  Test:
    def __init__(self):
        self.a=10
        self.b=20
        #a and b are instance object variable

t1=Test()
#Test() is nothing but __init__(t1)
print(t1.a)

'''



'''
#how to creare list object
l1=[10,20,30,40]
type(l1)
#tuple-(),set-{},list-[],dict-{key:value},str-"",int-10,float-10.5,bool-True/False,complex-10+20j
print(type(l1))

l2=[40,True,'shashank-',10.5,10+20j] #list can store any type of data-hetrogenous
print(l2[0] ,l1[2] ,l2[-1])# we can access the element of the list by using index in list

'''

#Accessing list elements via for loop
'''
l1=[50,39,80,10,60,40]
for x in l1:
    print(x,end=" ")

'''

#Accessing list elements via while loop from both side of the list
'''
l1=[50,39,80,10,60,40,6000]
i=0
while (i<=5):
    print(l1[i],end=' ')
    i+=1


l2=[50,39,80,10,60,40,6000]
i=5
while (i>=0):
    print(l2[i],end=' ')
    i-=1

    '''
# how to delete an element from the list
'''
l3=[10,20,30,40,50,60]
del l3[2] #deleting element from the list
print (l3)
'''

# how to edit an element from the list
'''
l1=[10,20,30,40,50,60]
l1[2]=300# in place of 30 we are replacing 300
# l1[6]=600 # we can not add element in the list by using index
print(l1)#[10, 20, 300, 40, 50, 60]
l1.append(70)# we can add element in the list by using append method [10,20,30,40,50,60,70]
l1.insert(1,999)# we can add element in the list by using insert method [10,999,20,30,40,50,60,70] there will not be replacement 20 will be shifted to forward
l1.insert(100,1000) # 80 is the index and 1000 is the element [10,999,20,30,40,50,60,70,1000] if index > lastindex then value will be stored at last index +1 

'''

# loop based problem 
# while loop is used when u want to run the code in loop only untill the code is true
# break is used to break the loop it will exit the loop
# for loop is on iterable sequence like list,tuple,string,dict it will not work on int float bool

for i in range(1,11):
    print(2*i-1,end=" ")
    i+=1
print()