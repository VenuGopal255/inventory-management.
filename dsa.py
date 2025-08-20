#dsa-data structures and algorithams
#sorting techinies
#linear saerch example
x=[3,6,2,5,8,0,9,4,1,7]
ele=int(input('enter element'))
for i in range(0,len(x)+1):
    if x[i]==ele:
        print(ele,'found')
        break
else:
    print('not found')

#binary saerch example
x=[3,6,2,5,8,0,9,4,1,7]
x.sort
start=0
end=len(x)-1
mid=(start+end)//2
while True:
    if start>end:
        print('start is very biggers')
    elif x[mid]==ele:
        print(ele,'found')
        break
    elif x[mid]<ele:
        start=mid+1
    elif x[mid]>ele:
        end=mid-1
    else:
        pass

#insert
#ex: 
x=[1,2,3,4]
x.insert(1,10)
print(x)
#without using insert funct
x=[1,2,3,4]
x[:1]+10+x[1:]
print(x)
#to add str
x=[10,20,True,'sita']
ele=input('enter element:')
idx=int(input('enetr index no:'))
op=x[:idx]+[ele]+x[idx:]
print(op)

#selection sort
x=[1,4,5,7,2,3,56,7,8,9]
for i in range(0,len(x)):
    min_val=min(x[i:])
    idx=x[i:].index(min_val)+i
    x[i],x[idx]=x[idx],x[i]
print(x)

#bubble sort
x=[1,4,5,7,2,3,56,7,8,9]
for i in range(len(x)):
    for j in range(0,len(x)-i-1):
        if x[j]>x[j+1]:
            x[j],x[j+1]=x[j+1],x[j]
print(x)

#quicksort
x = [5, 3, 8, 4, 2, 7, 1, 10]
if len(x)<=1:
    sortedx=x
else:
    pivot=x[0]
    left=[]
    right=[]
    for i in range(1,len(x)):
        if x[i]<pivot:
            left.append(x[i])
        else:
            right.append(x[i])
    left.sort()
    right.sort()
    sortedx=left+[pivot]+right
print(sortedx)