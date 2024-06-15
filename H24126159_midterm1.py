i = 9	#從9開始，後面的數
j = 9	#前面的數
while i >= 1:
	while j >= 1:
		k = 0
		while k <= 2: #一列三行
			print(j,"x",i-k,"=",(j*(i-k)),end="\t") #印出第一行
			k += 1 #第二行和第三行
		print() #換下一行
		j -= 1
	print() #換下一行
	i -= 3
	j = 9  #j回到9