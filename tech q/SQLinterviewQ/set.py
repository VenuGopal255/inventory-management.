#SET := it is a data structure which allows hetrogenious values,which does not follow order and not allow duplicates which is 
# immutable and used for only set theory operations..

#1 Q
'''
1. Remove Duplicates from List Using Set
Problem:
Given a list with duplicate elements, convert it to a set to get only unique elements.

Example:

python
Copy
Edit
Input: [1, 2, 2, 3, 4, 4, 5]
Output: {1, 2, 3, 4, 5}
'''
#Ans
'''
x= [1, 2, 2, 3, 4, 4, 5]
y=set(x)
print(y)'''

#2 Q
'''
2. Set Operations (Union, Intersection, Difference)
Problem:
Given two sets:

python
Copy
Edit
a = {1, 2, 3, 4}  
b = {3, 4, 5, 6}
'''
#Ans
'''
a = {1, 2, 3, 4}  
b = {3, 4, 5, 6}
c=a|b
c=a-b
c=a&b
print(c)'''

#3 Q
'''
3. Check Subset and Superset
Problem:
Check whether one set is a subset or superset of another.

Example:

python
Copy
Edit
3. Check Subset and Superset
Problem:
Check whether one set is a subset or superset of another.

Example:

python
Copy
Edit
a = {1, 2, 3}  
b = {1, 2, 3, 4, 5}
'''
#Ans
'''
a = {1, 2, 3}  
b = {1, 2, 3, 4, 5}
c=a.issubset(b)
d=a.issuperset(b)
print(c,d)'''

#4 Q
'''
4. Find Common Elements Between Two Lists
Problem:
Using sets, find the common elements between two lists.

Example:

python
Copy
Edit
list1 = [1, 2, 3, 4]  
list2 = [3, 4, 5, 6]  
Output: {3, 4}
'''
#Ans
'''
list1 = [1, 2, 3, 4]  
list2 = [3, 4, 5, 6]  
c=(set(list1))&(set(list2))
print(c)'''

#5 Q
'''
5. Print Unique Words in a Sentence
Problem:
Write a Python program to extract and print all unique words from a sentence.

Example:

python
Copy
Edit
Input: "Python is fun and Python is powerful"
Output: {'Python', 'is', 'fun', 'and', 'powerful'}'''
#Ans
'''
x= "Python is fun and Python is powerful"
y=x.split()
z=set(y)
print(y)'''
