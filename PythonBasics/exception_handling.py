#Exception Handling
try:
    a=10/0
except ZeroDivisionError:
    print("Can't Divide by Zero")
else:
    print("Divisible by zero")
finally:
    print("Execution Completed")

