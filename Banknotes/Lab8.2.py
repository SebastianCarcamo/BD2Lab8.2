import math

def ED(x,y):
	sum = 0
	for i in range(len(x)):
		sum += (float(x[i]) - float(y[i]))**2
	return math.sqrt(sum)


def rangeSearch(Q,r,C):
	result = []

	for i in range(len(Q)):
		Q[i] = str(Q[i])

	while Q in C:
		C.remove(Q)


	for i in C:
		dist = ED(Q,i)
		if dist < r:
			result.append(i)
	return result

def KNN(Q,k,C):
	result = []

	for i in range(len(Q)):
		Q[i] = str(Q[i])

	while Q in C:
		C.remove(Q)

	
	for i in C:
		dist = ED(Q,i)
		result.append([i,dist])

	result.sort(key=lambda x: x[1])
	result = [item[0] for item in result]
	return (result[0:k])


def PR(x, result):
	retrieved = float(len(result))
	relevant = 0.0
	if x in bamba:
		authentication = bamba
	else:
		authentication = firme


	for i in result:
		if all(j in authentication for j in [x,i]):
			relevant +=1

	return relevant/retrieved

data = []
bamba = []
firme = []

with open('./data_banknote_authentication.txt') as file:
	for line in file:
		aux = []
		num = line.split(',')
		for i in range(len(num)-1):
			aux.append(num[i])

		if num[-1] == '0\n':
			bamba.append(aux)
		else:
			firme.append(aux)

		data.append(aux)

print(len(bamba))

q300 = data[300]
q900 = data[900]
q1337 = data[1337]
r1 = 2
r2 = 6
r3 = 9


# print(PR(q300,rangeSearch(q300,r3,data)))
# print(PR(q900,rangeSearch(q900,r3,data)))
# print(PR(q1337,rangeSearch(q1337,r3,data)))


print(PR(q300,KNN(q300,32,data)))
print(PR(q900,KNN(q900,32,data)))
print(PR(q1337,KNN(q1337,32,data)))