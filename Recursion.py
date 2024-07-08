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
