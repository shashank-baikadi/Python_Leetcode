#x is being accessed by Demo.py file
x=10000000
'''
y=input("Enter a number: ")

#Type casting or connverting the string into integer
z=12+int("5")
print(z)
#binary conversion
bin(x)
d=bin(x)
print(bin(x))
#octal conversion
oct(x)

#how to find out ASCII code value of a character
ord('A')

# ASCII code value to character
chr(65)

'''



'''
if x==10000000:
    print("hello shashank")
    print('baikadi')
  
else:
    print("x is not equal to 10000000")

'''



# write a program to check wheather a number is positive or not

''' 
y=int(input("Enter a number: "))
if y>0:
    print("enter number is positive")
if y<0:
    print("enter number is negative")
else:
    print("enter value no number value ")

'''

# write a program to print grade obtained in a test .take marks from user and display the grade 
#90 < marks <=100       A
# 80 < marks <=90       B
# 70 < marks <=80       C 
# 60 < marks <=70       D
# 50 < marks <=60       E
# below 50              F
'''
y=int(input("enter a number : "))
if y>90 & y<=100:
    print("A")
elif y>80 & y<=90:
    print("B")
elif y>70 & y<=80:
    print("C")
elif y>60 & y<=70:
    print("D")
elif y>50 & y<=60:
    print("E")
else:
    print("F")
'''

# write a program to check wheather a number is even or odd

'''
y=int(input("enter a number "))

#print("even" if y%2==0 else "odd   )
if y%2==0:
    print("even")
else:
    print("odd")

'''

# write a program to print shashank five times on the screen using while loop
'''
i=1
while 1<=5:
    print("shashank")
    i+=1

'''
# write a program to print first n natural number 
'''
e=int(input("enter a number :"))
i=1
while i<=e:
    print(i)
    i+=1
    
'''


# write a program to print sum of first N  natural number