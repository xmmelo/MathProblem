class point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def midpoint(self, other):
        return point((self.x + other.x)/2, (self.y + other.y)/2)