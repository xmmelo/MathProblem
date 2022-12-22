import random
import statistics
from Models.point import *

class quadrilateral:
    
    def __init__(self, vertices):
        self.vertices = vertices
        self.xValues = self.getVerticeAllX()
        self.yValues = self.getVerticeAllY()
        self.midX = self.getMidX()
        self.midY = self.getMidY()

    def getVerticeAllX(self):
        return [o.x for o in self.vertices]
    
    def getVerticeAllY(self):
        return [o.y for o in self.vertices]

    def getMidX(self):
        return statistics.mean(self.xValues)

    def getMidY(self):
        return statistics.mean(self.yValues)
        
    def split(self):

        randomNumber = random.randint(0, 1)

        if(randomNumber%2):
            return [quadrilateral([self.vertices[0], point(self.midX, self.vertices[0].y), self.vertices[1], point(self.midX, self.vertices[1].y)]), 
                    quadrilateral([point(self.midX, self.vertices[2].y), self.vertices[2], point(self.midX, self.vertices[3].y), self.vertices[3]])]
        else:
            return [quadrilateral([self.vertices[0], self.vertices[1], point(self.vertices[0].x, self.midY),  point(self.vertices[1].x, self.midY)]), 
                    quadrilateral([point(self.vertices[2].x, self.midY), self.vertices[2], point(self.vertices[3].x, self.midY), self.vertices[3]])]