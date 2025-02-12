#Control Statements


print("If Statement")
a="hello"
b="hello"
if a == b:
    print("Equal")

print("if else Statement")
a=10
b=20
if a == b:
    print("Equal")
else:
    print("Not Equal")

print("elif Statement")
a=20
if a == 5:
    print(5)
elif a == 10:
    print(10)
elif a == 15:
    print(15)
elif a == 20:
    print(20)
else:
    print("Not Exist")

#Looping
print("For Looping")
a=[]
for i in range(10):
    a.append(i)
print(a)

print("While Looping")
i=10
a=[]
while i>0:
    a.append(i)
    i-=1
print(a)

#Continue and Break Statements
print("For Loop with Break")
for i in range(10):
    if i == 3:
        break
    print(i)

print("For Loop with Continue")
a=[]
for i in range(10):
    if i == 3:
        continue
    a.append(i)
print(a)
