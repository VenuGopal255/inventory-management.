#  TUPLE:- its a datastructure ,which allows hetrogenious values and follows order which is immutable..
#1 Q
'''
1. Tuple Indexing & Slicing
Problem:
Given the tuple:

python
Copy
Edit
t = (10, 20, 30, 40, 50)
Print:

The first element

The last element

A slice containing the middle three elements
'''
'''

t = (10, 20, 30, 40, 50)
print(t[0])
print(t[-1])
print(t[1:4])'''
#2 Q
'''
2. Swap Values Using Tuple
Problem:
Write a Python program that swaps the values of two variables using a tuple.

Example:

python
Copy
Edit
a = 5  
b = 10 '''
#Ans
'''
a = 5  
b = 10

a,b = b,a
print(a,b)'''

#3 Q
'''
3. Tuple Unpacking
Problem:
Given a tuple with 3 elements:

python
Copy
Edit
info = ("Alice", 25, "Engineer")
Unpack the tuple into individual variables: name, age, and profession, and print them.
'''
#ans
'''
info = ("Alice", 25, "Engineer")
name,age,study=info
print('name:',name)
print('age:',age)
print('study:',study)'''

#4 Q
'''
4. Count Elements in Tuple
Problem:
Given a tuple of integers:

python
Copy
Edit
nums = (1, 2, 3, 2, 4, 2, 5)
Write a program to count how many times 2 appears in the tuple'''
#ANS
'''
nums = (1, 2, 3, 2, 4, 2, 5)
cnt=nums.count(2)
print(cnt)'''

#5 Q
'''
5. Convert List of Tuples to Dictionary
Problem:
Convert the following list of tuples into a dictionary:

python
Copy
Edit
data = [("apple", 2), ("banana", 3), ("orange", 1)]
'''
#Ans
'''
data = [("apple", 2), ("banana", 3), ("orange", 1)]
dic=dict(data)
print(dic)'''