print("121910313053","Jithendra Naidu")
def postfix(exp):
    s=[]
    for i in exp:
        if i.isdigit():
            s.append(i)
        else:
            a = s.pop()
            b = s.pop()
            s.append(str(eval(b+i+a)))
    return s.pop()
exp = str(input("Enter an expression:"))
val = postfix(exp)
print("Required value is : ")
print(val)
