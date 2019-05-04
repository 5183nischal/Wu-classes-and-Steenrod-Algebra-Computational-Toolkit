from pbadem import pbresult
from adem import result
# inp = [[8,8,8]]
# print(result(inp))

p = 5
rng = 4
print("p=",p)
print("#########")
if p == 2:
	Q = [[[1]]]
	for i in range(1,rng):
		for j in Q[i-1]:
			temp = [[2**i]+j, j+[2**i]]
		red_temp = result(temp)
		Q.append(red_temp)
else: #really the bulk of work here due to bokstein prime
	Q = [[[-1,1]]]
	for i in range(rng):
		temp = []
		for j in Q[i]:
			# print("j=", j)
			temp += [[p**i]+j, j[0:len(j)-1]+[p**i]+[-1*j[len(j)-1]]]
			# print("temp=",temp)
			red_temp = pbresult(temp)
		#print (temp, "temp vs red_temp", red_temp)
		Q.append(red_temp)

def render(x):
	if p ==2:
		exp = ""
		for i in x:
			for j in i:
				exp += "Sq^{"+str(j)+"}"
			exp += " + "
		return exp[:-2]


	else:
		exp = ""
		count = 0
		for i in x:
			if i[-1] != 0:
				if i[-1] <-1:
					exp +=  " " +str(int(i[-1]))
				if i[-1] == -1:
					exp +=  " - "
				if i[-1] >0 and count >0:
					exp +=  " + " + str(int(i[-1]))
				for j in i[0:len(i)-1]:
					if j >0:
						exp += " P^{" + str(j) + "}"
					if j <0:
						exp += " \\beta"
			count += 1
		return exp



count = 0
for k in Q:
	#print(k)
	print("Q_{" + str(count) + "} = ", render(k))
	print("\\\\")
	count += 1
