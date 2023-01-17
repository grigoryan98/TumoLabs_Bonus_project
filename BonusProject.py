from time import sleep

def countdown(inp):
	while True:
		if inp[0] == inp[1] == inp[2] == 0:
			break
		elif inp[2] == 0 and inp[1] == 0:
			inp[0] -= 1
			inp[2] = inp[1] = 59
		elif inp[2] == 0:
			inp[1] -= 1
			inp[2] = 59
		else:
			inp[2] = inp[2] - 1

		ls = inp.copy()
		for i in range(len(ls)):
			if ls[i] // 10 == 0:
				ls[i] = "0" + str(ls[i])
			else:
				ls[i] = str(ls[i]) 

		st = ':'.join(i for i in ls)
		print(st)
		sleep(0.3)


inp = input("Insert time to countdown style. (00:00:00)\n>>> ").strip()
inp = inp.split(':')
try:
	for i in range(len(inp)):
		inp[i] = int(inp[i])
	if (len(inp) == 3 and 0 <= inp[0] <= 23 and 0 <= inp[1] <= 59 and 
		0 <= inp[2] <= 59):
		countdown(inp)
	else:
		("invalid input")
except:
	print("invalid input")

