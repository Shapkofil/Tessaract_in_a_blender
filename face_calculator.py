import math 

def compute(x,y):
	result = [x]
	for i in range(3):
		result.append([x[i],x[i+1],y[i],y[i+1]])
	result.append([x[0],x[3],y[0],y[3]])
	result.append(y)
	return result

cube = compute([0,1,2,3],[4,5,6,7])
tessaract = cube [:]
for face in cube:
	for newface in compute(face,[x+8 for x in face]):
		if not newface in tessaract:
			tessaract.append(newface)

print(tessaract)

print(len(tessaract))
