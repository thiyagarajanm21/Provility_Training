#DATA TYPES
r=10
print(type(r))

r=10.0
print(type(r))

r=10==20
print(type(r))

r="String"
print(type(r))



#Range Type
r = range(6)
print(list(r))

#List
r = [10,20,30,40,50]
print(r)

#List Operations
print("Insertion Operation: Insert 60 ")
r.append(60)
print(r)

print("Insert 15 at 1th position")
r.insert(1,15)
print(r)

print("remove value 15 ")
r.remove(15)
print(r)

print("remove at 5th position")
r.pop(5)
print(r)

r1=[90,89,70,60]
print("Sorting a list")
r1.sort()
print(r1)

print("Reverse a list")
r.reverse()
print(r)

print("Slicing from 1 to 5")
print(r[1:4])



#Tuple
r = ("john","mick","edvin")
print(r)

#Tuple Operations
print("Access Element in Tuple:")
print(r[1])

print("Slicing from 1 to 2")
print(r[1:2])


print("Unpacking")
x,y,z=(1,2,3)
print(x)

#Dictionary
r={1:"john",2:"mick",3:"edvin"}
print(r)

#Dictionary Operations
print("Updating Dictionary from john to ram")
r[1]="ram"
print(r)

print("Getting values")
print(r.get(2))

print("Removing ")
print(r.pop(1))

print("Getting Keys")
print(r.keys())

print("Getting Values")
print(r.values())

print("Getting dictionary as an items")
print(r.items())

#set
r={1,2,3,4,5,"edvin"}
print(r)

#Set Operations
print("Adding 6")
print(r.add(6))

print("Pop ")
r.pop()
print(r)

print("Remove")
r.remove(3)
print(r)

print("Discard")
r.discard(6)
print(r)

