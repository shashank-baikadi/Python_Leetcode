#if u want to access the x value which is in Test.py file in Demo.py file then u have to import the Test.py file in Demo.py file
import Test
import keyword

print("there are total",len(keyword.kwlist),"keywords in python")
print(keyword.kwlist)

# if u want to access x from Test.py file use the file name in front of x
print(Test.x)


print("provide in put for a and b")
# int(input()) is used to take input from the user
a=int(input())
b=int(input())
c=a+b
print("sum of a and b is",c)

#type() is used to find the type of the variable
print(type(c))