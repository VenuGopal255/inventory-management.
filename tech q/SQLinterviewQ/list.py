#1. LIST:- list ia a datastructure which allows homogeneous values,which follows order and allows dupliate values 
#           and it mutable in terms of adding ,removing and modifing...


#(1). Write a program to calculate the sum of all elements in a list.?
'''
nums = [5, 10, 15, 20]
s=0
for i in nums:
    s+=i
print(s)

# using sum method
print(sum(nums))
'''

#(2). Write a function to find the maximum element in a list without using max().?
'''
nums = [3, 7, 2, 9, 5]
max_val=0
for i in nums:
    if i>max_val:
        max_val=i
print(max_val)

# using max method
print(max(nums))
'''

#(3). Write a program that removes all duplicate values from a list while keeping the original order.?
'''
nums = [1, 2, 2, 3, 1, 4, 3]
original=[]
duplicate=[]
for i in nums:
    if i not in original:
        original.append(i)
    else:
        duplicate.append(i)
print(original)
print(duplicate)
'''

#(4). Write a function to reverse a list without using [::-1] or reverse().?
'''
nums = [10, 20, 30, 40]
rev=[]
for i in nums:
    rev=[i]+rev
print(rev)
'''
#(5). Given a list of numbers, return a new list containing the square of each number.?
'''
nums = [1, 2, 3, 4]
op=[i**2 for i in nums]
print(op)
'''