import bpy
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

#hyper-parameters 
n_frames = 125 

#making an instance of Tessaract
tessaract = Tessaract()

#making a blender object
hypermesh = bpy.data.meshes.new("hyperCube")
hyperobject = bpy.data.objects.new("hyperCube",hypermesh) 
hyperobject.location = bpy.context.scene.cursor.location
bpy.context.collection.objects.link(hyperobject)
hypermesh.from_pydata(tessaract.project(),[],tessaract.faces)
hypermesh.update(calc_edges = True)

#formating the raw data form Tessaract
data = []
for frame in range(n_frames):
    data.append(tessaract.project_raw(2))
    tessaract.rotate((np.pi*2)/n_frames)

#converting the data to shapekeys
for i_frame in range(n_frames):
    block = hyperobject.shape_key_add(name = "HyperState.{0}".format(i_frame),from_mix= False)
    block.value = 1.0
    block.mute = True 
    for (v,co) in zip(block.data,data[i_frame]):
        v.co = co

    # set up key frames
    block.mute = True
    block.keyframe_insert(data_path = "mute",frame = 0,index =-1)
    
    block.mute = False
    block.keyframe_insert(data_path = "mute",frame = i_frame + 1,index =-1)
    
    block.mute = True
    block.keyframe_insert(data_path = "mute",frame = i_frame + 2,index =-1)