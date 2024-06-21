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


#how to creare list object
l1=[10,20,30,40]
type(l1)
#tuple-(),set-{},list-[],dict-{key:value},str-"",int-10,float-10.5,bool-True/False,complex-10+20j
print(type(l1))

l2=[40,True,'shashank-',10.5,10+20j] #list can store any type of data-hetrogenous
print(l2[0] ,l1[2] ,l2[-1])# we can access the element of the list by using index in list