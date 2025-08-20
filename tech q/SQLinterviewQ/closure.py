# 1. CLOSURE:- it is remembering stag of a vriable outside of a function is know as closure..
'''
def make_counter():
    count=0
    def counter():
        nonlocal count
        count +=1
        return count
    return counter
c1=make_counter()
print(c1())
print(c1())

c2=make_counter()
print(c2())
'''

#2
'''

def outer(msg):
    def inner():
        print ('message:',msg)
    return inner
closure=outer('this is closure hai..')
closure()

'''