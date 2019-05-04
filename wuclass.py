from scipy.special import comb
import pickle


def sqMul(a,b):
	temp = []
	
	for i in a:
		for j in range(len(b)):
			temp.append(b[j] +i)
	if len(a) != 0 and len(b) != 0:
		return temp
	else:
		return []

def SrSq(i, W):
	sq = []
	if len(W) == 1:	#end for recursion
		j = W[0]
		for t in range(i+1):
			temp = comb(j-i+t-1, t)
			if t == 0 and i ==j: temp =1
			if temp%2 != 0:
				if i - t != 0:
					sq.append([i-t,j+t])
				else:
					sq.append([j+t])
	elif len(W) >1:
		for t in range(i+1):
			#print(SrSq(t,[W[0]]), "//", SrSq(i-t,W[1:]) )
			add = sqMul(SrSq(t,[W[0]]),SrSq(i-t,W[1:]))
			sq += add
			#print(add)
	return sq

# eg = [2,2]
# a = SrSq(1,eg)
# print(a)

def render(x, n):
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

	ans = 'v_{' + str(n) + '} = '
	part_1 = ''
	part_0 = ''
	for j in char:
		#if not "w_{1}" in j and not "w_{2}" in j:
		if "w_{1}" in j:
			part_1 += j + " + "
		else:
			part_0 += j + " + "
	ans += "(" + part_1[:-2] + ") + " + part_0
	return ans[:-2]






'''
k = 6
v = [0]*k
wu = [0]*k
v[1] = [[1]]
wu[1] = [[1]]
for i in range(2,k):
	rng = i//2
	v[i] = [[i]]
	for j in range(1,rng+1): #wu's theorem range
		for k in wu[i-j]: # linear seperation of v_k-1
			v[i] += SrSq(j,k)
			#if i ==5 : print("k = ", i-j, "//", SrSq(j,k))

	for j in range(len(v[i])): #sorting
		v[i][j] = sorted(v[i][j])
	#print(sorted(v[4]))

	wu[i] = []
	for j in v[i]:
		#print(j, "count = ", v[i].count(j))
		if v[i].count(j) % 2 != 0: 
			if j not in wu[i]: wu[i].append(j)
	wu[i] = sorted(wu[i])
		

eg = [2,2]
a = SrSq(1,eg)
print(a)
length = []
itemlist = []
p = 2
for i in range(18):
	print(render(wu[p],p))
	print("\\\\")
	print("\\linebreak")
	length.append(len(wu[p]))
	itemlist.append(wu[p])
	p += 1

print(length)

with open('outfile', 'wb') as fp:
    pickle.dump(itemlist, fp)
'''