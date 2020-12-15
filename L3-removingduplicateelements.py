print("121901313053","Jithendra Naidu")
l1=[] 
n=int(input("Enter array/list size:"))
for i in range(0,n):
    l1.append(int(input("Enter element:")))
print("Original list/array:",l1)
res=[]
for i in l1:
    if i not in res:
        res.append(i)
print("New array is:",res)
