from scipy.special import comb
import pickle

# x= [i,j], 0<i<2j

p = 3 #a prime

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

inp = [[1,1,1]]

def calc(inp):
	ans = []
	for x in inp: # iterate through sq1sq2 + sq8
		out = []
		print("the x is:", x)
		if len(x) == 3: #checking the length of the monomial
			out = adem(x)
		elif len(x)>3:
			for i in range(len(x)-2): #-2 because the last term is a coefficient
				count = 0
				print(x[i] , p*x[i+1])
				if x[i] < p*x[i+1]: #coparing two consecutive
					count += 1
					temp= adem([x[i],x[i+1]])
					print("temp", temp)
					for k in temp:
						temp_coef = k.pop()
						k = x[0:i] + k + x[i+2:len(x)-1] +[temp_coef*x[len(x)-1]]
						print(k)
						out.append(k)
					break # stop after finding 1 consecutive
			if count == 0:
				out.append(x) # if no consecutive error
		ans += out
	return ans


def result(inp):
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
			print(i)
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

print(result(inp))





