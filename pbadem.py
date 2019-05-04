from scipy.special import comb
import pickle

# x= [i,j], 0<i<2j

p = 5 #a prime

def adem(x):
	ans = []
	i = x[0]
	j = x[1]
	if i <p*j:
		for k in range((i//p) +1):
			temp = ((-1)**(i+k))*comb((j-k)*(p-1)-1,i-p*k)
			# if temp%2 != 0:
			ans.append([i+j-k, k, temp%p])
	else:
		ans.append(x)
	return ans

def b_adem(x):
	ans = []
	i = x[0]
	j = x[1]
	if i <= p*j:
		for k in range((i//p) +1):
			temp = ((-1)**(i+k))*comb((j-k)*(p-1),i-p*k)
			ans.append([-1,i+j-k, k, temp%p])

		for k in range((i//p) +1):
			temp = ((-1)**(i+k-1))*comb((j-k)*(p-1),i-p*k-1)
			ans.append([i+j-k,-1, k, temp%p])
	else:
		ans.append(x)
	return ans

inp = [[5,-1,8,1]]

def calc(inp):
	ans = []
	for x in inp: # iterate through sq1sq2 + sq8
		out = []
		#print("the x is:", x)
		if len(x) == 3 and not -1 in x[0:len(x)-1]: #checking the length of the monomial
			out = adem(x)
		elif len(x) == 3 and -1 in x[0:len(x)-1]: #checking the length of the monomial
			out.append(x)
		elif len(x)>3:
			for i in range(len(x)-2): #-2 because the last term is a coefficient
				count = 0
				#print(x[i] , p*x[i+1])
				##########
				if x[i] != -1 and x[i+1] != -1:
					if x[i] < p*x[i+1]: #coparing two consecutive
						count += 1
						temp= adem([x[i],x[i+1]])
						#print("temp", temp)
						for k in temp:
							temp_coef = k.pop()
							k = x[0:i] + k + x[i+2:len(x)-1] +[temp_coef*x[len(x)-1]]
							#print(k)
							out.append(k)
						break # stop after finding 1 consecutive
				elif x[i] == -1 and x[i+1] == -1:
					count += 1
					out.append([])
					break
				elif x[i] != -1 and x[i+1] ==-1 and i+2 <=len(x)-2:
					if x[i] <+ p*x[i+2]: #coparing two consecutive skipping the bockstein
						count += 1
						temp= b_adem([x[i],x[i+2]])
						#print("temp", temp)
						for k in temp:
							temp_coef = k.pop()
							k = x[0:i] + k + x[i+3:len(x)-1] +[temp_coef*x[len(x)-1]]
							#print(k)
							out.append(k)
						break # stop after finding 1 consecutive


				######

			if count == 0:
				out.append(x) # if no consecutive error
		ans += out
	return ans


def pbresult(inp):
	a = calc(inp)
	#print(a)


	# print(a)
	temp = []	
	while a != temp:
		temp = a
		a = calc(a)
		# print("loops")
		#print(a)

	result = []
	final = []
	for i in a:
		temp_coef = i.pop()
		while 0 in i:
			i.remove(0)
			#print(i)
		i.append(temp_coef)
	for i in a:
		mul = 0
		for j in a: #Field of order 2
			if i[0:len(i)-1] == j[0:len(j)-1]:
				mul += j[len(j)-1]

		result.append(i[0:len(i)-1] + [mul])

	for i in result:
		if not i in final:
			final.append(i)

	return final

#print(result(inp))
# print(b_adem([5,8]))





