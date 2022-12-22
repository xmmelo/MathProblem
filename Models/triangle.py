import random

class triangle:
    
    def __init__(self, vertices):
        self.vertices = vertices
        self.mainVertice = self.getMainVertice()
        self.commonVertices = self.getCommonVertices()
        self.midPoint = self.getMidPoint()

    def getMainVertice(self):
        #Generates a random number between 0 a 2
        verticeNumber = random.randint(0, 2)
        return self.vertices[verticeNumber]

    def getCommonVertices(self):
        temp = self.vertices.copy()
        temp.remove(self.mainVertice)
        return temp

    def getVerticeX(self, index):
        return self.vertices[index].x
    
    def getVerticeY(self, index):
        return self.vertices[index].y

    def getMidPoint(self):
        return self.commonVertices[0].midpoint(self.commonVertices[1])        
        
    def split(self):
        return [triangle([self.commonVertices[0], self.midPoint, self.mainVertice]), triangle([self.commonVertices[1], self.midPoint, self.mainVertice])]
