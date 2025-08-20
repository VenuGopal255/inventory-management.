#1  .Write a program that uses a while loop to print numbers from 1 to 10.
'''
x=11
i=0
while i<x:
    print(i)
    i+=1
'''
#  2. Sum of Digits of a Number?
'''
x=1234
s=0
while x>0:
    i=x%10
    s+=i
    x=x//10
print(s)
'''

# 3. Reverse a Number?
'''
x=1234
op=0
while x>0:
    i=x%10
    op=op*10+i
    x=x//10
print(op)
'''

#  4. Check Palindrome Number?
'''
x=121
xx=x
y=0
while x>0:
    i=x%10
    y=y*10+i
    x=x//10
if y==xx:
    print('palandrome')
else:
    print('not palandrome')
'''

# 5. Guess the Number Game?
'''
import random

num = random.randint(1, 10)
attempts = 5

while attempts > 0:
    guess = int(input('Enter a number (1–10): '))
    if guess == num:
        print(f"{num} — your guess is correct 🎉")
        break
    elif guess < num:
        print('Guess is too low')
    else:
        print('Guess is too high')

    attempts -= 1

if attempts == 0:
    print(f"Sorry, you ran out of attempts! The number was {num}.")
'''
 

        



