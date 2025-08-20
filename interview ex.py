#paradigiam - style of coding
#1
'''
def add(a,b):
    c=a+b
    return c

def sub(a,b):
    c=a-b
    return c

def mul(a,b):
    c=a*b
    return c

def div(a,b):
    c=b/a
    return c

def main():
    print('1.addition')
    print('2.subtration')
    print('3.multiplication')
    print('4.div')

    ch=int(input("enter your choice:"))
    n1=int(input('enter n1:'))
    n2=int(input('enter n2:'))

    if ch==1:
        res=add(n1,n2)
        return res
    
    elif ch==2:
        res=sub(n1,n2)
        return res
    
    elif ch==3:
        res=mul(n1,n2)
        return res

    else:
        res=div(n1,n2)
        return res
    
print(main())'''

#2 types of parameters
'''
1.positional arguments-normal parameters are called as positinal arguments.
2.default parameters/arguments(calling point of view)- when ever you dont want to pass any value you want to take default value .
3.keyword aruguments-when ever you dont want to follow the order mentioning before sending values then goes to respective parameter.
4.list of aruguments-if u want to send n no of argument in this situation we use this.
5.dict of keyword arguments(**kwargs):key and value n no of pairs we use dict arguments
ex:def display(**kwargs):
    peint(**kwargs)
display(name='gopi',age=24,add='kmm')
'''
#example for parameters
'''
def display(a,b,*args,d='*',**kwargs):
    print('mandatory inputs:',a,b)

    if len(*args)>0:
        print('optional arguments')
        print(args)

    print('default:',d)

    if len(**kwargs)>0:
        print('dict of **kward args:')
        print(**kwargs)

display(10,'rama',20,'sita',True,name='gopi',age=24,add='kmm')'''

#3 GENERATOR:" it is a spl function which contain yield keyword to return op for mul times....""
#examples: 
'''
def even(start,end):
    for i in range(start,end+1):
        if i %2==0:
            yield i
res=even(1,11)
print(res)'''
        
#4.HEAP MEMORY-"it stores global variables "
#5.STACK MEMORY-"it stores func varaibles deletes after function is over"

#function- 
#example
'''
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
print(y)'''

#op=vCuBe

#scope- availabiblity of a variable within the function is known as scope
'''
def outer():
    print('chiru')
    def inner():
        print('balaya')
    return inner()
outer()'''

#closure:- remembering stag of a variable outside of  a function is known as closure
#example
'''
def outer():
    x=20
    def inner():
        print(x)
    return inner

f=outer()
f()'''

#permitations
'''
x=0
y=1
z=2
op=[li for li in [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1)] if sum (li)!=3]
print(op)'''

#variables= variables are building blocks of programing lang. used to store values
#example:
'''
x=10
y='gopi'
z=10.3'''

#datatypes: data types are classifications that define the kind of value a variable
'''
#1.int 
x=10
#2.float
z=10.3
#3 .string
z=10.3
#4.bool
is_name=True
#5.list:
x=[10,20]
#6tuple:
x=(10,20)
#7.dict:
z={'name':'gopi','age':24}'''

#shallow-which copy ele's along with addresses 
# ex:
'''
x=[1,2,3]
y=x
print(id(x))
print(id(y))
x.append(10)
print(x)
print(y)
'''
#deepcopy-which copy ele's along without addresses 
# ex:
'''
x=[1,2,3]
y=[]
y.extend(x)
print(x)
print(y)
x.append(10)
print(id(x))
print(id(y))
'''
#conditions: based on given condition can we take next step or not decideds by given condition
#if,else,elif

#loops :it used to itterate the giving condition for mutiple times.
#for: it literates the sequence
#while : it iterates until we get the answer 

#break : used to come out from the loop
#continue: it jumps from current iteration to next iteration

#data structres: it is used to store data in organised manner
#list:-list ia data structure it allows hetro genius values ,which allows duplicate values ,which follows order,which is mutable interms of adding,removing and modifing.
#tople:-A tuple is a data structure that Allows heterogeneous values,Allows duplicate values,which follows order,Is immutable (you cannot add, remove, or modify elements after creation).
#set:-setA set is a data structure that Allows heterogeneous values,Does not allow duplicate values,which Does not follows order,Is mutable (you can add or remove elements, but not modify them directly). 
# which are used for set theory operations:1.union(|),2.intersection(&),3.difference(-),4.symtrick diff(^)
#dict:-A dictionary is a data structure that Stores data as key-value pairs,Keys must be unique (values can be duplicated),which follows order,Is mutable (you can add, remove, or modify key-value pairs).
#str:string is a sequence of characters with are enclosed bt single,double and triple colums..

#positionsal arguments 
# ex:
'''
def add(a,b):
    c=a+b
    return c
res=add(10,20)
print(res)
'''
#defalut arguments 
# ex:
'''
def add(a,b=20):
    c=a+b
    return c
res=add(10)
print(res)
'''
#key word arguments 
'''
def add(a,b):
    c=a+b
    return c
res=add(10,20,30)
print(res)
'''
#isinstance- it is used to check the object is instance to a  specific class or a tuple of classes
'''
x=20
print(isinstance(x,int))'''

#self - it nothing but current obj in py.

#mro-method revolutionary order

#method overloading- it ntg but ability to define no of methods with same name but differnt parameter types and no of parameters
'''Python does not support true method overloading like Java or C++, where you define multiple methods with the same name but different parameter counts/types.
class Calc:
    def add(self, a, b, c=0):  # default argument
        return a + b + c

c = Calc()
print(c.add(2, 5))       # 7
print(c.add(2, 5, 3))    # 10

'''

#method overiding-method overriding occurs when subclass provides a spl implemntion method  which provided in its superclass which is altering its behaviour. 
# 2,ex: changing the method of base class from child class is known as methodoveridhing
'''
Method overriding means: a child class provides a different implementation of a method that already exists in its parent class.

class animal:
    def speck(self):
        print('animal makes sounds')
class dog(animal):
    def speck(self):
        print('bow bow')
class cat(animal):
    def speck(self):
        print('meow meow')
a=animal()
b=dog()
c=cat()

a.speck()
b.speck()
c.speck()
'''

#inheritance - it is acquring prpo's from one cls to another cls to create new class..
'''
class Calc:  # Parent class 
    def __init__(self, x, y): #constructor
        self.a = x #instance variable
        self.b = y

    def add(self): #instance variable
        return self.a + self.b

class AdvancedCalc(Calc):  # Child class inheriting from Calc
    def multiply(self):
        return self.a * self.b

obj = AdvancedCalc(10, 20)
print(obj.add())       # Inherited method → 30
print(obj.multiply())  # Child class method → 200

'''
#instance variable- it is used to store specific data to the particular obj is know as instance variable

#instance variable-it is particular to the specific data and its processes is konwn as instance variable

#factory method - it is used to create new obj of the cls without directly instancing the cls

#constructor - it is a spl method it automatically invocs when we called it used to initialzed the attributes of the class

#decorator - it used to modify the behaviour of the funct without modifying the fuct.
'''
def outer(fun):
    def inner():
        print('*'*10)
        fun()
        print('*'*10)
    return inner
@outer
def display():
    print('gopal.gopi')
display()
'''

#generator- it a spl funct which contain yield key word to return values for multiple times..
'''
def outer(start,end):
    for i in range(start,end+1):
        if i%2==0:
            yield (i)
res=outer(1,11)
for even in res:
    print(even)'''

#2 example
'''
def outer():
    num=1
    while True:
        yield (num)
        num+=1
        if num==10:
            return
res=outer()
for i in res:
    print(i)
'''

#abstraction= hiding implementational details from a user and providing user manual only.. 
# ex
'''

'''

#class- class is collection of variables and methods variables are used to collect the data and methods are used to proceses data it is a blue print..
#variables- it is real time entity it is an instance of class it had it own set of attributes and methods and which can used to proceeses and interact with it

#polymorpism- behaving differntly in diff situations.
#ex:
'''
class cat:
    def sounds(self):
        print ('meow meow')
class dog:
    def sounds(self):
        print ('bow bow')
class rat:
    def sounds(self):
        print ('kitch kitch')
def call(obj):
    obj.sounds()
    
c=cat()
d=dog()
r=rat()

call(r)
call(d)
call(c)

'''

#encapsulation - wrapping up data and method into single unit is known as ensapusaltion it is also called as class  and we can't acces or modifi the data from out side of fuct
# ex:
'''
class std:
    def __init (self,name,age):
        self.__name=name
        self.__age=age

    def info(self):
        return(self.__name+self)
s1=std('gopi',24)
s1.info()
'''
#recursion - a function which calling itself is known as recursion..
#ex:1
'''
def display(x=1):
    print(x)
    if x==10:
        return
    display(x+1)
display()
'''
#ex:2
'''
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
res=fact(5)
print(res)
'''

#exception handling - is ntg but run time error.. 3 types of errors -1.syntax error,2.logical errors,3.run time errors
#ex:1
'''
try:
    num=int(input('enter num:'))
    den=int(input('enter num:'))
    
    res=num//den
    print('division result is:'res)

except ZeroDivisionError:
    print('denominator should not be zero

except ValueError:
    print('value should be in interger')

except Exception:
    print('something went wrong')
    
else:
    print('division result is:'res)
    
finally:
    print('mandatory statement')
print('program is succesfuly completed')
'''
#3. Set Operations
'''
a = {1, 2, 3}
b = {3, 4, 5}'''

#questions:

#1.Find common elements
#2.Find elements only in a but not in b
#3.Check if they are disjoint sets

'''
print(a & b)
print(a - (b))
print(a.isdisjoint(b))'''