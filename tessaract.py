import numpy as np

class Tessaract:
    #constructor default case being a 2X2 tessaract 
    def __init__(self,dimentions = [[-1,-1,-1,-1],[1,1,1,1]],faces = [(6, 4, 12, 14), (8, 10, 14, 12), (2, 6, 14, 10), (0, 4, 6, 2), (10, 8, 0, 2), (4, 0, 8, 12), (4, 5, 7, 6), (13, 12, 14, 15), (7, 5, 13, 15), (15, 14, 6, 7), (5, 4, 12, 13), (7, 3, 11, 15), (2, 3, 11, 10), (14, 15, 11, 10), (3, 2, 6, 7), (8, 9, 13, 12), (10, 11, 9, 8), (13, 9, 11, 15), (9, 8, 0, 1), (1, 3, 11, 9), (1, 0, 2, 3), (5, 1, 9, 13), (1, 0, 4, 5), (1, 5, 7, 3)]):
        matrix = []
        #building 4D vertices matrix  
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    for w in range(2):
                        matrix.append([dimentions[x][0],dimentions[y][1],dimentions[z][2],dimentions[w][3]])
        self._vetices = np.asarray(matrix)
        self.faces = faces

    @property
    def vetices(self):
        return [(tuple(vertex))for vertex in self._vetices]

    #Double rotating by rad 
    def rotate(self,rad):
        rmatrix = Tessaract.calculate_rotation_matrix(rad)
        self._vetices = np.dot(rmatrix,self._vetices.T).T

    #calculating the rotation matrix for the given angle
    @staticmethod
    def calculate_rotation_matrix(rad):
        result = np.asarray([[np.cos(rad),-np.sin(rad),0,0],
                             [np.sin(rad),np.cos(rad),0,0],
                             [0,0,np.cos(rad),-np.sin(rad)],
                             [0,0,np.sin(rad),np.cos(rad)]])    
        return result

    #wrapper function 
    def project(self,lw = 2):
        projection = []
        for vertex in self.project_raw(lw):
            projection.append(tuple(vertex))
        return projection

    #making an np array with the vertex data of the shadow
    def project_raw(self,lw):
        projection = []
        for vertex in self._vetices:
            projected = np.dot(Tessaract.calculate_projection_matrix(vertex,lw),vertex.T).T
            projection.append(projected)
        return np.asarray(projection)

    #calculating projection matrix for every vertex
    @staticmethod
    def calculate_projection_matrix(vertex,lw):
        w = vertex[3]
        projection_coefficient = 1/(lw-w)
        primitive_matrix = np.asarray([[1,0,0,0],[0,1,0,0],[0,0,1,0]])
        return projection_coefficient*primitive_matrix
            
#testing the module
if __name__ == "__main__":
	tessaract = Tessaract([[-1,-1,-1,-1],[1,1,1,1]])
	tessaract.rotate(np.pi*2)
	print(tessaract.project())


		