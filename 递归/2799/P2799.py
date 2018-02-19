c = input()
sign = 0
list = []
for i in c:
	list.append(i)

if len(list)%2 == 0:
	while True:
		number_long = len(list)
		middle = number_long//2
		if number_long%2 == 1:
			break
		for i in range(middle):
			if list[i] == list[number_long-i-1]:
				continue
			else:
				sign = 233
				break
		if sign == 233:
			break
		else:
			for i in range(middle):
				list.pop()

shortest = len(list)
print(shortest)
