#STRING:- string is a sequence of characters with are enclosed bt single,double and triple colums..
#1 Q
'''
1. Reverse a String
Problem:
Write a Python program to reverse the given string.

Example:

python
Copy
Edit
Input: "hello"
Output: "olleh"
'''
#Ans
'''
x='hello'
y=''
for i in x:
    y=i+y
print(y)'''

#2 Q
'''
2. Count Vowels in a String
Problem:
Write a Python function that counts the number of vowels (a, e, i, o, u) in a string.

Example:

python
Copy
Edit
Input: "Programming is fun"
Output: 5
'''
#Ans
'''
x= "Programming is fun"
y='aeiou'
cnt=0
for i in x:
    if i in y:
        cnt+=1 
print(cnt)'''

#3 Q
'''
3. Check for Palindrome
Problem:
Write a Python program to check if a string is a palindrome (reads the same forwards and backwards).

Example:

python
Copy
Edit
Input: "madam"
Output: True
'''
#Ans
'''
x= "madam"
y=x[::-1]
print(x==y)'''

#4 Q
'''
4. Remove Duplicate Characters
Problem:
Write a Python program to remove duplicate characters from a string, keeping only the first occurrence.

Example:

python
Copy
Edit
Input: "aabbccdde"
Output: "abcde"
'''

#Ans
'''
x= "aabbccdde"
y=''
for i in x:
    if i not in y:
        y+=i
print(y)'''

#5 Q
'''
5. Most Frequent Character
Problem:
Write a Python program to find the most frequently occurring character in a string (excluding spaces).

Example:

python
Copy
Edit
Input: "hello world"
Output: "l"
'''

#Ans
'''
x= "hello world"
y= x.replace(' ','')
z={}
for i in y:
    z[i]=z.get(i,0)+1
most=max(z,key=z.get)
print('most repeated chr:',most)
'''

