'''
dict is a class
its mutable
not a sequence
is iterable
indexing is not pplicable to dict object
dict element are pai of key-value and data-value
slicing operator is not applicatbel


in side set all value are key which cant be duplicate where as in dict we have key-data pair
'''
d1={1:'one',2:'two',3:'three'}
print(d1)
print(type(d1))

#empty dict
d2={}
print(d2)   
print(type(d2))


#create a d3 dict object
d3=dict()

d4=dict(a='shashank',b='baikadi')
print(d4)

# accessing dict elements
print(d1)
print(d1[1],d1[2])

for k in d1:
    print(k,d1[k]) # print key and value 


'''
edit the element

edit means you want to change data-value of nthe element and not the key-value
dictObject[key-value]=newdatavalue

delete
del d1[102]

add
dictionaryObject[new-key-value]=data-value
d1[102]='hundred two'

methods
items()-collects dict elements 
keys()-collection of keys  only of the elements
values()-collection of data-value only of the elements

get()
pop()
popitem()
clear()
copy()


'''

d4.keys() # returm the keys of the dict object
d1.values() # return the values of the dict object
d1.items() # return the key-value pair of the dict object
