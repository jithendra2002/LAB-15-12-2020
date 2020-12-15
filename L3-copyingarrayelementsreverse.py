print("Jithendra-121910313053")
a=[]
n=int(input("enter number of elements to be entered into array"))
for i in range(0,n):
    i=int(input("enter the element"))
    a.append(i)
print("original array is:",a)
b=[None]*len(a)
l=len(a)
for i in range(0,l):
    b[i]=a[l-i-1]
print("new array is:",b)    
