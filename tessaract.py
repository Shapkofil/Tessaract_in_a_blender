import numpy as np
import math

class Tessaract:
	def __init__(self,dimentions = [[-1,-1,-1,-1],[1,1,1,1]]):
		matrix = []
		for x in range(2):
			for y in range(2):
				for z in range(2):
					for w in range(2):
						matrix.append([dimentions[x][0],dimentions[y][1],dimentions[z][2],dimentions[w][3]])
		self.vertecies = np.asarray(matrix)

	@staticmethod
	def calculate_rotation_matrix(degree):
		result = np.asarray([[np.cos(degree),-np.sin(degree),0,0],
			[np.sin(degree),np.cos(degree),0,0],
			[0,0,1,0],
			[0,0,0,1]])	
		return result
	

	def rotate(self,degree):
		rmatrix = Tessaract.calculate_rotation_matrix(degree)
		self.vertecies = np.dot(rmatrix,self.vertecies.T).T

	@staticmethod
	def calculate_projection_matrix(vertex,lw):
		w = vertex[3]
		projection_coefficient = 1/(lw-w)
		primitive_matrix = np.asarray([[1,0,0,0],[0,1,0,0],[0,0,1,0]])
		return projection_coefficient*primitive_matrix


	def project(self,lw):
		projection = []
		for vertex in self.vertecies:
			projected = np.dot(Tessaract.calculate_projection_matrix(vertex,lw),vertex.T).T
			projection.append(projected)
		return np.asarray(projection) 

if __name__ == "__main__":
	tessaract = Tessaract([[-1,-1,-1,-1],[1,1,1,1]])
	print(tessaract.vertecies)
	tessaract.rotate(math.pi*2)
	print(tessaract.vertecies)
	print(tessaract.project(2))


		