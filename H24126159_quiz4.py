s = input("Enter a sequence of integers seperated by whitespace:")
lst=s.split(" ")
h=[] 
for k in lst: # 把輸入的數字轉換成list
	k = int(k)
	h+=[k]
# print(h)

lics = [] # 一個空的list放要輸出的數字

# for i in range(len(h)):
# 	if int(h[i]) < int(h[i+1]):
# 		lics.append(h[i])
# print("Length:",len(lics))
# print(lics)

i=0
while i < len(h)-1: 
	if h[i]<h[i+1]: # 後面一個如果比當下的數字還要大
		lics.append(i) # 就把數字放進lics的這個list裡面
	i+=1
print("Length:",len(lics)) # 印出lics的長度
print(lics) # 印出lics

# for i in h:
# 	if i < i+1:
# 		lics.append(i)
# print("Length:",len(lics))
# print(lics)