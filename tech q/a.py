'''write a py prog to find and return all substr's of a str that are palindrome'''
x='madam'
for i in range(len(x)):
    for j in range(i+1,len(x)+1):
       sub= x[i:j]
       if sub==sub[::-1]:
            print(sub,end=',')

#3 write a py prog to grp a list of words into anagrams
x=['listen','silent','enlist','hello','ohile']
op={}
for i in x:
    key=''.join(sorted(i))
    if key in op:
        op[key].append(i)
    else:
        op[key]=[i]
res=(list(op.values()))
print(res)

#write a py prog to find the longest word in sentence that is not pal?
x='my mom and dad saw a racer today'
j=x.split()
long=''
for word in j:
    if word!=word[::-1]:
        if len(word)>len(long):
            long=word
print(long)

#binary
x=13
print(bin(x)[2:])
# recursion fun
def binary(x):
    if x==0:
        return ''
    else:
        return binary(x//2)+str(x%2)
print(binary(13))

#function
def change(s):
    op=''
    for i in range(0,len(s)):
        if i%2==0:
            acode=ord(s[i])
            if acode>=97 and acode<=122:
                op=op+chr(acode-32)
            else:
                op=op+s[i]
        else:
            op=op+s[i]
    return op
x='vucbe'
y=change(x)
print(y)

#op=vCuBe

#permitations...
import random
x='abc'
y=list(x)
op=[]
while True:
    random.shuffle(y)
    z=''.join(y)
    if z not in op:
        op.append(z)
    if len(op)==6:
        break
print(op)

#advanced method
import itertools
x='abc'
op=[''.join(y) for y in itertools.permutations(x)]
print(op)

#char count
x='apple'
op={}
for i in x:
    op[i]=op.get(i,0)+1 / op[i]=x.count(i)
print(op)

#flattern

x = [1, 2, [3, 4, [5, 6], 7, 8], 9, 0]

op=[]
def flattern(y):
    for i in y:
        if type(i)==list:
            flattern(i)
        else:
            op.append(i)
flattern(x)
print(op)

#3. Set Operations
a = {1, 2, 3}
b = {3, 4, 5}
#questions:
'''
1.Find common elements
2.Find elements only in a but not in b
3.Check if they are disjoint sets
'''
print(a&b)
print(a.difference(b))
print(a.isdisjoint(b))

'''4. Write a Python function to check if a string is a palindrome or not.
Example: "madam" → True, "hello" → False'''
x='madam'
y=''
for i in x:
    y=i+y
if y==x:
    print('palandrome')
else:
    print('not')
      
#find the runnerup score ?
x=[20,-25,2,6,30,9,1]
first=float('-inf')
second=float('-inf')
for i in x:
    if i>first:
        second=first
        first=i
    if i>second and first>i:
        second=i
print('runner up score:',second)

#find longsest consequtive no?
x={1,10,4,3,2,}
long=0
for i in x:
    if i-1 not in x:
        cur=i
        length=1

        while cur+1 in x:
            cur+=1
            length+=1
        if length>long:
            long=length
print(long)

    