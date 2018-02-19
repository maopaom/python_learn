c = input()
list = []
for i in c:
	list.append(i)

while True:
	number_long = len(list)
	middle = number_long//2
	if list[middle] == list[middle-1]:
		for i in range(middle):
			list.pop()
	else:
		break

shortest = len(list)
print(shortest)
