library={}

def add_book():
	add = input("Enter the title, genre, and the price of the book (separated by ,):") # abc,p,200
	add = add.split(",")
	add = [str(x) for x in add]
	# print(add)
	print("Add",add[0],"to the library.")
	price="%0.2f" % float(add[2])
	library[add[0]]=add[1],price # library={abc:P, 200.00}
	# print(library)
	for key,value in library.items():
		# print(value[1])
		print(str(key) + " (" + str(value[0]) + ", $" + str(value[1]) + ")")
	print()
	
def remove_book():
	remove = input("enter the title of the book to remove:")
	if remove not in library:
		print("\nError:",remove,"is not found in library.")
	else:
		del library[remove]
		for key,value in library.items():
			print(str(key) + " (" + str(value[0]) + ", $" + str(value[1]) + ")")
	print()


def get_book_info():
	info = input("Enter the title of the book:")
	if info not in library:
		print("\nError:",info,"is not found in library.")
	else:
		print("\nTitle:",info,"\nGenre:",library[info][0],"\nPrice: $",library[info][1])
	print()

def list_all_books():
	for key,value in library.items():
		print(str(key)+" ("+str(value[0])+",$"+str(value[1])+")")
	print()
	# print("\n",library,"\n")

def list_books_by_genre():
    genre = input("Enter the genre to search for: ")
    genre_books = [(key, value) for key, value in library.items() if value[0] == genre]
    if not genre_books:
    	print("\nNo books found in",genre,"genre.\n")
    else:
    	for key,value in genre_books:
    		print(str(key)+" ("+str(value[0])+",$"+str(value[1])+")")
    print()

choice=""
while choice!="quit":
	print("Menu:\n1. Add a book\n2. Remove a book\n3. Get book information\n4. List all books\n5. List books by genre\n6. Quit")
	choice=input("Enter your choice (1-6):")
	if choice=="1":
		add_book()
	elif choice=="2":
		remove_book()
	elif choice=="3":
		get_book_info()
	elif choice=="4":
		list_all_books()
	elif choice=="5":
		list_books_by_genre()
	elif choice=="6":
		print("Goodbye!")
		break

# add = input("Enter the title, genre, and the price of the book (separated by ,):") # abc,p,200
# add = add.split(",")
# add = [str(x) for x in add]
# # print(add)
# print("Add",add[0],"to the library.")
# print(add[0],"(",add[1],", $%.2f)"% float(add[2])) 