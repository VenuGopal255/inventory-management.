# LIST COMP:= it is used to create short way of list
# 1Q
'''
square of even numbers?
'''
# Ans
'''
x=[1,2,3,4,5,6]
op=[i**2  for i in x if i%2==0]
print(op)'''

#2 Q
'''
return a string which have more than 3 char using list comp ?
'''
# ANS
'''
x=['gopi','uma','roa','priya']
op=[i for i in x if len(i)>3]
print(op)'''

#3 Q
'''
give a list of temp's in cel's convert them to fehrent using the formula f=(c*9/5)+32 using list comp?
'''
# Ans
'''
x=[0,5,10,15,30,32]
op=[(i*9/5) for i in x]
print(op)'''

#4 Q
'''
remove vowels from a word using list comp ?
'''
# Ans
'''
x='gopi'
y='aeiou'
op=[i for i in x if i not in y]
print(op)'''

#5 Q
'''
create a list of tuples (x,x**) for all the even nu's between 1 and 10 using list comp?  
'''
# Ans
'''
x=[1,2,3,4,5,6,7,8,9,10,11]
op=[(i,i**2) for i in x if i%2==0]
print(op)'''