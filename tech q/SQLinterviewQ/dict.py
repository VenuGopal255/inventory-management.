# DICT: it a data structuire which follows order and does not allow duplicates and stores data as a key value pairs

#1 Q
'''
1. Count Frequency of Elements in a List
Problem:
Given a list of elements, use a dictionary to count how many times each element appears.

Example:
Input: ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']  
Output: {'apple': 3, 'banana': 2, 'orange': 1}
'''
#ANS
'''
x= ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']  
y={}
for i in x:
    if i not in y:
        y[i]=1
    else:
        y[i]+=1
print(y)'''

#2 Q
'''
2. Merge Two Dictionaries
Problem:
Given two dictionaries, merge them into one. If a key exists in both, add their values.

Example:

python
Copy
Edit
dict1 = {'a': 10, 'b': 20}  
dict2 = {'b': 5, 'c': 30}  
Output: {'a': 10, 'b': 25, 'c': 30}
'''
#Ans
'''
x = {'a': 10, 'b': 20}  
y = {'b': 5, 'c': 30}
merge=y.copy()
for k,v in x.items():
    merge[k]=merge.get(k,0)+v
print(merge)'''

#3 Q
'''
3. Find Key with Maximum Value
Problem:
Given a dictionary with numeric values, find the key with the highest value.

Example:

python
Copy
Edit
data = {'math': 90, 'science': 85, 'english': 92}  
Output: 'english'
'''
#ans
'''
x = {'math': 90, 'science': 85, 'english': 92}  
y=min(x.keys())
print(y)'''

#4 Q
'''
4. Swap Keys and Values
Problem:
Given a dictionary, swap its keys and values.

Example:

python
Copy
Edit
Input: {'a': 1, 'b': 2, 'c': 3}  
Output: {1: 'a', 2: 'b', 3: 'c'}
'''
#Ans
'''
x= {'a': 1, 'b': 2, 'c': 3}  
y={v:k for k,v in x.items()}
print(y)'''

#5 Q
'''
5. Create Dictionary from Two Lists
Problem:
Given two lists — one with keys and one with values — create a dictionary.

Example:

python
Copy
Edit
keys = ['id', 'name', 'age']  
values = [101, 'Alice', 25]  
Output: {'id': 101, 'name': 'Alice', 'age': 25}
'''
#ans
'''
x = ['id', 'name', 'age']  
y = [101, 'Alice', 25]  
res=dict(zip(x,y))
print(res)'''

#   ZERO TO HERO BOOK DICT Q/A:
#1
my_dic={}
my_dic['name']='venu'
print(my_dic)
print(my_dic['name'])

#2
print(my_dic['name'])
#3
(my_dic['age'])=24
(my_dic['name'])='venu gopal'
print(my_dic)
#4
remov=my_dic.pop('age')
print(my_dic)
print(remov)
#5
my_dict = {'a': 1, 'b': 3, 'c': 5, 'd': 2}
op={k:v for k,v in my_dict.items() if v>1 }
print(op)
