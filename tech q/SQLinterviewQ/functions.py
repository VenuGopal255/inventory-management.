# 1. functions paalandeome string ?

'''
def is_pal(word):
    word = word.lower()
    return word == word[::-1]
print(is_pal('madam'))
print(is_pal('py'))
'''

#2 factorial using recursion ?

'''
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
print(fact(0))
'''

#3  using functions cnt vowels in str?
'''
def cnt_vol(s):
    vol='aeiou'
    return sum(1 for char in s if char in vol)
print(cnt_vol('gopi'))'''

# 4 fabonaci series? using functions?
'''
def febo(n):
    fec=[0,1]
    while len(fec)<n:
        fec.append(fec[-1]+fec[-2])
    return fec[:n]
print(febo(5))
'''
#5 find max using functions in py?
'''
def maxi(n):
    max_val=0
    for i in n:
        if i>max_val:
            max_val=i
    return max_val
nos=[1,1,9,5,2]
print(maxi(nos))
'''
