# lambda is a keyword 
# lamda expression are syntactically restricted to a single expressiom\
# lambda input:expression
# lambda a,b:a+b
# no need to of def keyword

lambda a,b:a+b
add=lambda a,b:a+b
print(add(2,3))


f1=(lambda a,b:a+b)(10,20)
print(f1)

#Recursion using Lambda
#calucalate factorial of a number using recursion lambda expression 

#normal
def fact(n):
    if n==0 or n==1:
        return 1
    
    return n* fact(n-1)

# Using LambdaExpression
f=lambda n: 1 if n==1 or n==1 else n*f(n-1)
print(f(5))