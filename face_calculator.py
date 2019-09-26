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
tessaract.extend(compute([8,9,10,11],[12,13,14,15]))
for face in cube:
	for newface in compute(face,[x+8 for x in face]):
		if not newface in tessaract:
			tessaract.append(newface)

print(sorted(tessaract,key = lambda x: (x[0],x[1],x[2])))

print(len(tessaract))
