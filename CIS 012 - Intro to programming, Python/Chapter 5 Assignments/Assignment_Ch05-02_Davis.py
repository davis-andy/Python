n = 121
i = 0
x = 0
MT = []
flag = True

while flag == True:
	while i < (n+1):
		MT.append(i)
		i += 1
	while MT[x] < n:
		if MT[x] == 0:
			print("Multiplication Table:\nX", end = "\t")
			x += 1
		elif 0 < MT[x] < 10:
			print(MT[x], end = "\t")
			x += 1
		elif MT[x] == 10:
			print(MT[x], end = "\n")
			x += 1
		elif MT[x] == 11:
			print(MT[x]-10, end = "\t")
			x += 1
		elif 11 < MT[x] < 21:
			print(((MT[x]-11)*1), end = "\t")
			x += 1
		elif MT[x] == 21:
			print(((MT[x]-11)*1), end = "\n")
			x += 1
		elif MT[x] == 22:
			print(MT[x]-20, end = "\t")
			x += 1
		elif 22 < MT[x] < 32:
			print(((MT[x]-22)*2), end = "\t")
			x += 1
		elif MT[x] == 32:
			print(((MT[x]-22)*2), end = "\n")
			x += 1
		elif MT[x] == 33:
			print(MT[x]-30, end = "\t")
			x += 1
		elif 33 < MT[x] < 43:
			print(((MT[x]-33)*3), end = "\t")
			x += 1
		elif MT[x] == 43:
			print(((MT[x]-33)*3), end = "\n")
			x += 1
		elif MT[x] == 44:
			print(MT[x]-40, end = "\t")
			x += 1
		elif 44 < MT[x] < 54:
			print(((MT[x]-44)*4), end = "\t")
			x += 1
		elif MT[x] == 54:
			print(((MT[x]-44)*4), end = "\n")
			x += 1
		elif MT[x] == 55:
			print(MT[x]-50, end = "\t")
			x += 1
		elif 55 < MT[x] < 65:
			print(((MT[x]-55)*5), end = "\t")
			x += 1
		elif MT[x] == 65:
			print(((MT[x]-55)*5), end = "\n")
			x += 1
		elif MT[x] == 66:
			print(MT[x]-60, end = "\t")
			x += 1
		elif 66 < MT[x] < 76:
			print(((MT[x]-66)*6), end = "\t")
			x += 1
		elif MT[x] == 76:
			print(((MT[x]-66)*6), end = "\n")
			x += 1
		elif MT[x] == 77:
			print(MT[x]-70, end = "\t")
			x += 1
		elif 77 < MT[x] < 87:
			print(((MT[x]-77)*7), end = "\t")
			x += 1
		elif MT[x] == 87:
			print(((MT[x]-77)*7), end = "\n")
			x += 1
		elif MT[x] == 88:
			print(MT[x]-80, end = "\t")
			x += 1
		elif 88 < MT[x] < 98:
			print(((MT[x]-88)*8), end = "\t")
			x += 1
		elif MT[x] == 98:
			print(((MT[x]-88)*8), end = "\n")
			x += 1
		elif MT[x] == 99:
			print(MT[x]-90, end = "\t")
			x += 1
		elif 99 < MT[x] < 109:
			print(((MT[x]-99)*9), end = "\t")
			x += 1
		elif MT[x] == 109:
			print(((MT[x]-99)*9), end = "\n")
			x += 1
		elif MT[x] == 110:
			print(MT[x]-100, end = "\t")
			x += 1
		elif 110 < MT[x] < 120:
			print(((MT[x]-110)*10), end = "\t")
			x += 1
		else:
			print(((MT[x]-110)*10), end = "\t")
			x += 1
	flag = False
