class Point:
    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y

    def __str__(self):
        return f"({self._x}, {self._y})"
    
    def __eq__(self, other):
        if not isinstance(other, Point): return False
        if self._x == other.x and self._y == other.y:
            return True
        return False
    
    def __add__(self, other):
        if not isinstance(other, Point):
            raise TypeError("Not valid types")
        return Point(self._x + other.x, self._y + other.y)
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        self._x = x
        
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        self.y = y

def are_equals(point1, point2):
    return point1 == point2

def add_points(point1, point2):
    return point1 + point2