print("Welcome to the simple calculator program!")

while True:
	a = float(input("Enter the first number:"))
	b = float(input("Enter the second number:"))
	which = input("Select an arithmetic operation(+, -, *, /):")
	#如果分母是0
	if b == 0 and which == "/":
		print("Division by zero!")
		continue

	elif which == "+":
		result = float(a + b)
		print("Result:",result)

	elif which == "-":
		result = float(a - b)
		print("Result:",result)

	elif which == "*":
		result = float(a * b)
		print("Result:",result)

	elif which == "/" and b != 0:
		result = float(a / b)
		print("Result:",result)

	#如果在運算符號選擇時輸入的不是+-*/時，重新輸入
	else:
		continue

	choise = input("Do you want to perform another calculation?(yes or no):")
	#選擇是否繼續運算
	if choise == "yes":
		continue
	if choise == "no":
		print("Goodbye!")
		break

