# k = int(input("Enter the size of the grid:"))
# for i in range(k):
# 	print("_ "*(k-1)+"_")
# 	print("")

# coordinates = str(input("Enter the cell coordinates to edit:"))
# y=int(coordinates[0]) #直
# x=int(coordinates[2]) #橫
# # print(直,橫)
# value = str(input("Enter the new value for the cell:"))

# for j in range(0,k-1):
# 	if j == y:
# 			print("_ "*x+value+" "+"_ "*(k-x-1-1)+"_")
# 	print("_ "*(k-1)+"_")

# j=0
# while j < k-1:
# 	if j == y:
# 		print("_ "*x+value+" "+"_ "*(k-x-1-1)+"_")
# 	print("_ "*(k-1)+"_")
# 	j += 1

###############################################
n = int(input("Enter the size of the grid: "))

# construct a 2-d matrix with dimension n
matrix = [["_" for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()
    # you can also use the below code to replace line 31 ~ line 33
    # print(" ".join(matrix[i]))

cell_coordinate = ""
new_value = ""

while cell_coordinate != "done":
    row, col = 0, 0
    cell_coordinate = input("Enter the cell coordinates to edit: ")
    if cell_coordinate == "done":
        break
    else:
        row, col = cell_coordinate.split(",")
        row, col = int(row), int(col)
    new_value = input("Enter the new value for the cell: ")

    # update the matrix value
    matrix[row][col] = new_value

    for i in range(n):
        print(" ".join(matrix[i]))