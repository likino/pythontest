def bubble(n):
	flag = True
	for i in range(len(n)-1, 0, -1):
		if flag:
			flag = False
			for j in range(i):
				if n[j] > n[j+1]:
					n[j], n[j+1] = n[j+1], n[j]
					flag = True
		else:
			break
				
	print n
			
n = [25, 5, 44, 33, 11, 1]
bubble(n)