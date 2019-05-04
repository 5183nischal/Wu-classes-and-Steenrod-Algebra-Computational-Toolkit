from wuclass import SrSq

def render(x):
	char = []
	for i in x:
		pos = 0
		j = 0
		expr = ''
		mul = 0
		while pos < len(i):
			if mul > 1:
				expr += "w_{" +str(i[pos])+ "}^{" + str(mul)+"}"
			elif mul == 1:
				expr += "w_{" +str(i[pos])+ "}"
				#print(expr)
			pos += mul
			mul = 0
			for j in range(len(i)-pos):
				#print(i[pos+j], "//", i[pos])
				if  i[pos+j] == i[pos]:
					mul +=1
				else:
					break
			#print(pos)
		char.append(expr)

	ans = ''
	part_1 = ''
	part_0 = ''
	for j in char:
		#if not "w_{1}" in j and not "w_{2}" in j:
		if "w_{1}" in j:
			part_1 += j + " + "
		else:
			part_0 += j + " + "
	ans += part_0			#part_1[:-2] + " + " + part_0
	return ans[:-3]


rng = 17
bundle = []

for i in range(1,rng):
	if i%2 == 1:
		exp = ''
		sr = SrSq(int((i-1)/2),[i])
		temp_1 = sr
		temp_2 = []
		for j in sr:
			temp_2.append([1]+j)
		exp = "\\mathfrak{P}(w_{"+str(i)+"}) = " + "\\beta_{4}(" + render(temp_1) + ") + \\theta_{2}(" + render(temp_2) +")"
		print(exp)
		print("\\\\")
	else:
		exp = ''
		sr = SrSq(i-1,[i])
		temp_1 = []
		for j in sr:
			temp_1.append([1]+j)
		temp_2 = []
		for k in range(int(i/2)):
			if k ==0:
				temp_2.append([2*i-2*k])
			else:
				temp_2.append([2*k,2*i-2*k])
		# print("1:", temp_1)
		#print("2:", temp_2)
		exp = "\\mathfrak{P}(w_{"+str(i)+"}) = " + "\\rho_{4}p_{" + str(int(i/2)) +"} + " + "\\beta_{4}(" +render([[i-1,i]]) +") + " 

		exp += "\\theta_{2}(" + render(temp_1) + render(temp_2) +")"
		print(exp)
		print("\\\\")







