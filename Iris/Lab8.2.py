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
	if x in setosa:
		specie = setosa
	elif x in versicolor:
		specie = versicolor
	else:
		specie = virginica


	for i in result:
		if all(j in specie for j in [x,i]):
			relevant +=1

	return relevant/retrieved

data = []
setosa = []
versicolor = []
virginica = []

with open('./iris.data') as file:
	for line in file:
		aux = []
		num = line.split(',')
		for i in range(len(num)-1):
			aux.append(num[i])

		if num[-1] == "Iris-setosa\n":
			setosa.append(aux)
		elif num[-1] == "Iris-versicolor\n":
			versicolor.append(aux)
		else:
			virginica.append(aux)
		data.append(aux)


q15 = data[15]
q82 = data[82]
q121 = data[121]
r1 = 1
r2 = 3
r3 = 5


print(PR(q15,KNN(q15,32,data)))
print(PR(q82,KNN(q82,32,data)))
print(PR(q121,KNN(q121,32,data)))