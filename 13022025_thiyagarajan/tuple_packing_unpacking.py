#Tuple Packing
emp_one = "Harish"
emp_two = "Venkat"
emp_three = "Dinesh"
tuple_data_one = (emp_one,emp_two,emp_three)
print(tuple_data_one)
print()

#Tuple Unpacking
print("Tuple Unpacking")
tuple_data_two = (10,20,30)
print("Tuple :",tuple_data_two)
x,y,z= tuple_data_two
print("x :",x)
print("y :",y)
print("z :",z)
print()

print("Ignoring Values during packing")
data = (100, 200, 300, 400)
print("Tuple :", data)
print("Extracting first and last elements ignoring the rest")
first_element,*_,last_element = data
print(first_element,last_element)
print()

# Function to pack arguments into a tuple
def pack_into_tuple(*args):
    print(args)
pack_into_tuple(1, 2, 3)
pack_into_tuple("apple", "banana", "cherry")
print()

numbers = (1,2,3,4,5,6,7,8)
print("Tuple :",numbers)
first,second,*rest=numbers
print("Unpacking first,second elements from Tuple")
print(first,second)
print("Extented packing")
print(rest)

