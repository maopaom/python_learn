def dfs(step):
	global number
	global sign
	global number_list
	if(step == number):
		for i in range(number-1):
			print("    "+str(number_list[i]),end = '')
		print("    "+str(number_list[number-1]))
	for i in range(1,number+1):
		if sign[i] == 0:
			sign[i] = 1
			number_list[step] = i
			dfs(step+1)
			sign[i] = 0

	

number = input()
number = int(number)
sign = []
number_list = []
for i in range(number+1):
	sign.append(0)
	number_list.append(0)
dfs(0)
