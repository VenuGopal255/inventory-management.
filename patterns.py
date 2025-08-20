#heart shape 1
'''
for i in range(6):
    for j in range(7):
        if (i==0 and j %3!=0) or \
        (i==1 and j %3==0) or  \
        (i-j==2 or i+j==8):
            print('*',end='')
        else:
            print(' ',end='')
    print()

#2
n=6
for i in range(n//2,n,2):
    for j in range(1,n-i,2):
        print(' ',end='')
    for j in range(1,i+1,1):
        print('*',end='')
    for j in range(1,n-i+1,1):
        print(' ',end='')
    for j in range(1,i+1,1):
        print('*',end='')
    print()
for i in range(n,0,-1):
    for j in range(i,n,1):
        print(' ',end='')
    for j in range(1,i*2,1):
        print('*',end='')
    print()'''

#3 pyramid
'''
n=6
i=1
while i<n:
    print(' '*(n-i), '*'*(i*2-1))
    i+=1'''
#4 Right-angled triangle
'''
n=5
i=1
while i<n:
    print('*'*i)
    i+=1'''
#5 Inverted right-angled triangle
'''
n=5
i=1
while i<n:
    print('*'*(n-i))
    i+=1'''
#6 diamond
'''
n=5
for i in  range(1,n+1):
    print(' '*(n-i),'*'*(2*i-1))

for i in  range(n-1,0,-1):
    print(' '*(n-i),'*'*(2*i-1))'''

#number pattern
'''
n=5
for i in range( 1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()'''

#hallow half pattern
'''
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1 or j==i or i==n:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''

#reverse pyramid
'''
n=5
for i in range(n):
    print(' '*i,'*'*(2*(n-i)-1) )'''

#   HALLOW SQUARE ?
'''
n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''