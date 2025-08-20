#  1. SCOPE:- availability of a value with in the function is known as scope.
'''
x=10 #global value
def outer_func():
    x=30 #nonlocal value
    def inner ():
        x=20 #local value
        print(x)
    inner()
    print(x)
print(x)
outer_func()
'''