import random
suits = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alpha = random.choice(suits) # 隨機出現一個要被猜的字母
print(alpha)

for i in range(len(suits)): # alpha的index設為i
		if suits[i]==alpha:
			alpha_index = i
			# print(int(i))
		if suits[i]!=alpha:
			continue

guess_alpha = ""

count=0
while guess_alpha != alpha: # 當使用者沒有猜到
	guess_alpha = input("Guess the lowercase alphbet:") # 使用者輸入的值是guess_alpha
	
	if guess_alpha not in suits:
		print("Please enter a lowercase alphbet.")
		continue
	for j in range(len(suits)): # guess_alpha的index設為j
		if suits[j]==guess_alpha:
			guess_alpha_index = j
			print(guess_alpha_index)
	
	his1=0
	his2=0
	his3=0
	his4=0
	his5=0
	his6=0
	his7=0

	if guess_alpha_index <= 3:
		his1+=1
	if 3 < guess_alpha_index <= 7:
		his2+=1
	if 7 < guess_alpha_index <= 11:
		his3+=1
	if 11 < guess_alpha_index <= 15:
		his4+=1
	if 15 < guess_alpha_index <= 19:
		his5+=1
	if 19 < guess_alpha_index <= 24:
		his6+=1
	if 24 < guess_alpha_index:
		his7+=1

	if int(guess_alpha_index) > int(alpha_index):
		print("The alphabet you are looking for is alphabetically lower.")
	if int(guess_alpha_index) < int(alpha_index):
		print("The alphabet you are looking for is alphabetically higher.")
	if int(guess_alpha_index) == int(alpha_index):
		print("Congradulations!",end="")
	count+=1
print("You guessed the alphabet", "\"",alpha,"\"", "in", count,"times.")

print("Guess Histogram:")
print("a - d:","*"*his1)
print("e - h:","*"*his2)
print("i - l:","*"*his3)
print("m - p:","*"*his4)
print("q - t:","*"*his5)
print("u - x:","*"*his6)
print("y - z:","*"*his7)