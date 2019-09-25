import numpy as np

class Tessaract(object):
	vertex = []

	def __init__(self,dimentions = [[-1,-1,-1,-1],[1,1,1,1]]):
		matrix = []
		for x in range(2):
			for y in range(2):
				for z in range(2):
					for w in range(2):
						matrix.append([dimentions[x][0],dimentions[y][1],dimentions[z][2],dimentions[w][3]])
		self.vertex = np.asarray(matrix)

	@staticmethod
	def calculate_rotation_matrix(degree):
		result = asarray([[np.cos(degree),-np.sin(degree),0,0],
			[np.sin(degree),-np.cos(degree),0,0],
			[0,0,1,0],
			[0,0,0,1]])	
		return result
	

	def rotate(self,degree):
		rmatrix = calculate_rotation_matrix(degree)
		