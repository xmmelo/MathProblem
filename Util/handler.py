from Models.point import *
from Models.triangle import *
from Models.quadrilateral import *

triangles = []
quadrilaterals = []

def handleTriangle(canvas):
    points = [point(100, 300), point(100, 100), point(200, 200)]
    triangles = [triangle(points)]
    

    for i in range(0,10):        
        randomNumber = random.randint(0, len(triangles) - 1)       
        if(len(triangles) == 1):
            randomNumber = 0        
        selectedTriangle = triangles[randomNumber]
        triangles.remove(selectedTriangle)
        newTriangles = selectedTriangle.split()
        triangles = triangles + newTriangles

    for tri in triangles:
        canvas.create_polygon(  tri.getVerticeX(0), 
                                tri.getVerticeY(0),    
                                tri.getVerticeX(1), 
                                tri.getVerticeY(1), 
                                tri.getVerticeX(2), 
                                tri.getVerticeY(2), 
                                outline='black', 
                                fill='')


def handleQuadrilateral(canvas):
    points = [point(100, 100), point(100, 300), point(300, 300), point(300,100)]
    quadrilaterals = [quadrilateral(points)]
    

    for i in range(0,1):        
        randomNumber = random.randint(0, len(quadrilaterals) - 1)       
        if(len(quadrilaterals) == 1):
            randomNumber = 0        
        selectedquadrilateral = quadrilaterals[randomNumber]
        quadrilaterals.remove(selectedquadrilateral)
        newquadrilateral = selectedquadrilateral.split()
        quadrilaterals = quadrilaterals + newquadrilateral

    for quadr in quadrilaterals:


        canvas.create_polygon(  quadr.vertices[0].x, 
                                quadr.vertices[0].y,    
                                quadr.vertices[1].x,
                                quadr.vertices[1].y,
                                quadr.vertices[2].x,
                                quadr.vertices[2].y,
                                quadr.vertices[3].x,
                                quadr.vertices[3].y,
                                outline='black', 
                                fill='')
