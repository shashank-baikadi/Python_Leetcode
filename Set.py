s1={1,5,8,5}
type(s1)
print(s1,"squence is not preserved and duplicate value are not allowed it wont print Two type 5 it will discard second 5 ")
print(type(s1))

s3=set()
print(type(s3))

'''
build in methods 

len()
min()
max()
sum()
sorted()
any()
all()

'''
s2={1,5,8,5}
print(len(s2), 'length of set')
print(min(s2), 'minimum value of set')
print(max(s2), 'maximum value of set')
print(sum(s2),'sum of set')
print(sorted(s2),'sorted set it will return a list which will remove duplicate')
print(any(s2), 'any value of set')
print(all(s2), 'all value of set')


'''
concatenation and repetition operator 

set+set-not supported
set*int-not supported

COMPARISON operator
    s1>s2
    s1<s2
    s1==s2
    s1!=s2
    s1>=s2
    s1<=s2
    all this supported

    two set bject are equal if their elements are same doesnt matter order of the elements
'''


'''
det object methods we can use the below method like this s1.add

add()
remove()
discard()
pop()
clear()
copy()
update()
union()
intersection()
difference()
symmetric_difference()
issubset()
issuperset()
isdisjoint()

'''

s5={10,50,80,51}
s5.add((66,67,68))
print(s5,'we can add iterable object in set')

s5.update((66,67,68))
print(s5,'in update the 66,67,68 will be added as individual element in s5')


'''
set comprehension
s1={expressionm for e in object}
s=input("enter a string")
s1={e for e in s if e in 'aeiou'}

^
|
for e in s:
if e in "aeiou":
a1.addd(e)


'''