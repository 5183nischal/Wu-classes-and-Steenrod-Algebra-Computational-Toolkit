from scipy.special import comb
import pickle

# x= [i,j], 0<i<2j

def adem(x):
	ans = []
	i = x[0]
	j = x[1]
	if i <2*j:
		for k in range((i//2) +1):
			temp = comb(j-k-1,i-2*k)
			if temp%2 != 0:
				ans.append([i+j-k, k])
	else:
		ans.append(x)
	return ans

inp = [[8,8,8]]

def calc(inp):
	ans = []
	for x in inp: # iterate through sq1sq2 + sq8
		out = []
		if len(x) == 2: #checking the length of the monomial
			out = adem(x)
		elif len(x)>2:
			for i in range(len(x)-1):
				count = 0
				if x[i] < 2*x[i+1]: #coparing two consecutive
					count += 1
					temp= adem([x[i],x[i+1]])
					for k in temp:
						k = x[0:i] + k + x[i+2:len(x)]
						out.append(k)
					break # stop after finding 1 consecutive
			if count == 0:
				out.append(x) # if no consecutive error
		ans += out
	return ans



def result(inp):
	a = calc(inp)
	# print(a)
	temp = []	
	while a != temp:
		temp = a
		a = calc(a)
		#print(a)

	result = []
	for i in a:
		if 0 in i:
			i.remove(0)
	for i in a:
		if a.count(i) %2 != 0 and not (i in result): #Field of order 2
			result.append(i)

	return result

#print(result(inp))





