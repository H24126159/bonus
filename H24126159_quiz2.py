A = int(input("Enter the shopping amount:"))
L = (input("Enter the membership level(Regular or Gold):"))
L = "Regular" or "Gold"
if L != "Regular" and L != "Gold": #如果membership輸入的不是gold也不是regular，print Invalid member level
	print("Invalid member level")
if A < 1000 and L == "Regular": #如果amount<1000且是Regular，沒有discount
	print(A)	
if 1000 <= A < 2000 and L == "Regular": #如果1000<=amount<2000且是Regular，10%off discount
	A= 0.9*A
	print(A)
if 2000 <= A < 3000 and L == "Regular": #如果2000<=amount<3000且是Regular，15%off discount
	A = 0.85*A
	print(A)
if 3000 <= A and L == "Regular": #如果3000<=amount且是Regular，20%off discount
	A = 0.8*A
	print(A)
if A < 1000 and L == "Gold":	#如果amount<1000且是Gold，no discount
	print(A)	
if 1000 <= A < 2000 and L == "Gold": #如果1000<=amount<2000且是Gold，15%off discount
	A= 0.85*A
	print(A)
if 2000 <= A < 3000 and L == "Gold": #如果2000<=amount<3000且是Gold，20%off discount
	A = 0.8*A
	print(A)
if 3000 <= A and L == "Gold": #如果3000<=amount且是Gold，25%off discount
	A = 0.75*A
	print(A)