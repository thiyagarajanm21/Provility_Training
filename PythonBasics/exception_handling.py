#Exception Handling
try:
    a=10/0
except ZeroDivisionError:
    print("Can't Divide by Zero")
else:
    print("Divisible by zero")
finally:
    print("Execution Completed")

# Exception Handling with Dictionary
try:
    d = {"car":"lexus"}
    print(d["bus"])
except KeyError:
    print("Key not found...")
else:
    print("Key found")
finally:
    print("Execution Completed")
