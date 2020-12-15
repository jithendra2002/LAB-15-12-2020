def binary_search(a,goal):
    low =0
    high=len(a)-1
    mid=(low+high)//2
    if a[mid]==goal:
        print(f' Element {goal} found at {mid}')
    elif a[mid]<goal:
        low=mid+1
        for i in range(low,high+1):
            if a[i]==target:
                print(f' Element {goal} found at {i}')
                break
    elif  a[mid]>goal:
        low=0
        high=mid
        for i in range(low,high):
            if a[i]==target:
                print(f' Element {goal} found at {i}')
                break
    else:
        print("Element not found")


n=int(input("Enter the size of array: "))
a=[]
for i in range(n):
    a.append(int(input("enter element:")))
a.sort()
print(a)
target=int(input("Enter the target to be searched:"))
binary_search(a,target)
