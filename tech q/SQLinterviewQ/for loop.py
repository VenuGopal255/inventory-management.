# 1 Print values from 1 to 10 in the format:?
'''
for i in range(1,11):
    print(i)
    '''

#2 2. ➗ Sum of multiples of 3 and 5?
'''
for i  in range(0,101):
    if i%3==0 and i%5==0:
        print(i)
'''

#3  3. 🔤 Count vowels in a string?
'''
x='a,e,i,o,u'
y='gopi'
for i in y:
    if i in x:
        print(i)
        '''
#4  4. 📺 Multiplication table generator?
'''
for i in range(1,11):
      print(f"5 * {i} = {5 * i}")
'''

#5  5. 🌟 Print prime numbers in a range?
'''
for i in range(1,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
'''
#6 string palandrome
x='madam'
op=''
for i in range(len(x)):
    op=x[i]+op
if op==x:
    print('palanderome')


   