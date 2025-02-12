add = lambda x,y:x+y
print(add(10,20))

# String Operation in lambda
full_name = lambda first_name,last_name:first_name+last_name
print(full_name("alex","smith"))

#Lambda Function with reduce
from functools import reduce
lst = [1,2,3,4]
product = reduce(lambda x,y:x*y , lst)
print(product)


customer = {"ram": 32000, "babu": 25000, "venkat": 15000}
hike_members = list(filter(lambda x: customer[x] > 20000, customer.keys()))
print(hike_members)






