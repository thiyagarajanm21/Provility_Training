#Slicing in List
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("List: ")
print(lst)
print("Extracting first five elements :")
print(lst[:5])
print("Extracting last five elements :")
print(lst[-5:])
print("Extracting every second elements :")
print(lst[1::2])
print("Reversing a list")
print(lst[::-1])

#String Slicing
print("String slicing")
sample_string = "PythonSlicing"
print("Extracting first 6 characters")
print(sample_string[:6])
print("Extracting last three characters")
print(sample_string[-3:])
print("Extracting every second character")
print(sample_string[1::2])
print("Extracting last three characters")
print(sample_string[::-1])

#Matrix Slicing
matrix =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for m in matrix:
    print(m)
print("Extracting first row from matrix")
print(matrix[0])
print("Extracting last column from matrix")
print([row[-1] for row in matrix])











