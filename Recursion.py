# function calling itself is called recursion.

def f():
    print('hi')
    # f()  
    print('bye')
f()

#Recursion tree

# how to dry run a code

def F1(n):
    if n==1:
        return 1
    s=n+F1(n-1)
    return s
x=F1(5)
print(x)


# write a recurion function to calulate sun of first n natural number
def sum(n):
    if n==1:
        return 1
    s=n+sum(n-1)
    return s
y=sum(10)
print(y)


# write a recurssive function to calculate sum of square of first n natural numbers
def sumsquare(n):
    if n==1:
        return 1
    s=n*n+sumsquare(n-1)
    return s
z=sumsquare(10)
print(z)