file_name="pe8_data.csv"
file=open(file_name,"r")
text=file.readlines()
# print(text)
file.close()

allteams=[] # 包含30支隊伍的list
for i in range(1,31):
	teams_info=text[i].split(',')
	allteams.append(teams_info)
# print(allteams)

# 1. 東區哪些球隊的主場勝率低於客場勝率
list1=[]
for i in range(30):
# len(allteams)=30
	if allteams[i][0]=="Eastern": 
		home=allteams[i][7] # home plc
		away=allteams[i][8] # away plc
		# print(home,away)
		home=home.split("-")
		# print(home)
		home_win,home_lose=int(home[0]),int(home[1])
		home_plc=home_win/(home_win+home_lose)
		# print(home_plc)
		away=away.split("-")
		away_win,away_lose=int(away[0]),int(away[1])
		away_plc=away_win/(away_win+away_lose)
		# print(away_plc)
		if away_plc>home_plc:
			list1.append(allteams[i][1])
print(list1)


# 2. 哪一區的球隊擁有較高的“平均得分減掉失分”
pf_sum_west=0
pa_sum_west=0
pf_sum_east=0
pa_sum_east=0
west_count=0
east_count=0
for i in range(30):
	pf = float(allteams[i][5])
	pa = float(allteams[i][6])
	if allteams[i][0] == "Western":
		pf_sum_west+=pf
		# print(pf_sum)
		pa_sum_west+=pa
		# print(pa_sum)
		west_count += 1
	elif allteams[i][0] == "Eastern":
		pf_sum_east+=pf
		pa_sum_east+=pa
		east_count += 1
west_avg_diff = ((pf_sum_west / west_count) - (pa_sum_west / west_count))
east_avg_diff = ((pf_sum_east / east_count) - (pa_sum_east / east_count))
# print(west_avg_diff,east_avg_diff)
if west_avg_diff > east_avg_diff:
	print("West conference had a higher average difference about “PF minus PA”.")
else:
	print("East conference had a higher average difference about “PF minus PA”.")


# 3. 根據每支球隊和另一區球隊的對戰紀錄來對所有球隊排序，對戰另一區擁有較高勝率的球隊會被排序在前面的位置
dict3={}
for i in range(30):
	WL = allteams[i][2].split("-")
	win, lose = int(WL[0]), int(WL[1])
	CONF = allteams[i][9].split("-")
	win_in_conf, lose_in_conf = int(CONF[0]), int(CONF[1])
	win_other_conf = win - win_in_conf
	lose_other_conf = lose - lose_in_conf
	dict3[allteams[i][1]]= win_other_conf/(win_other_conf+lose_other_conf)
teams_with_win_rates = [(team, win_rate) for team, win_rate in dict3.items()]
# print(teams_with_win_rates)
def sort_by_win_rate(item):
    return item[1]

# 按勝率排序
teams_with_win_rates.sort(key=sort_by_win_rate, reverse=True)

for team, win_rate in teams_with_win_rates:
    print(f"{team}: {win_rate:.3f}")
# print(dict3)
