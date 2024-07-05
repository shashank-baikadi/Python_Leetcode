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
'''
