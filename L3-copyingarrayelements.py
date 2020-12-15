print("Jithendra-121910313053")
a=[]
n=int(input("enter number of elements to be entered into array"))
b=[]
for i in range(0,n):
    x=int(input("enter the element:"))
    a.append(x)
print("original array is:",a)
l=len(a)
for c in range(0,l):
    x=a[c]
    b.append(x)
print("new array is:",b)   
