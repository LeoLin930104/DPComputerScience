import math

class Circle:
    def __init__( self, radius: float, cx: float = 0, cy:float = 0 ) -> None:
        self.radius = radius
        self.cx = cx
        self.cy = cy

    def area( self ) -> float:
        return math.pi * self.radius**2

    def circumference( self ) -> float:
        return math.pi * self.radius * 2

    def __str__( self ):
        return f"""Radius: { self.radius }, Area: { self.area() }, Circumference: { self.circumference() }, Cx = { self.cx }, Cy: { self.cy }"""
    
    def __eq__( self, other ) -> bool:
        return ( self.radius == other.radius ) and ( self.cx == other.cx ) and ( self.cy == other.cy )

    def __gt__( self, other) -> bool:
        return self.radius > other.radius

    def __ge__( self, other ) -> bool:
        return self.radius >= other.radius

    def __lt__( self, other ) -> bool:
        return self.radius < other.radius

    def __le__( self, other ) -> bool:
        return self.radius <= other.radius

    def __add__( self, other ) -> float:
        if type(other) is not Circle: raise TypeError("Must only add Circles together")
        
        new_radius = math.sqrt(self.radius**2 + other.radius**2)
        new_cx = (self.cx + other.cx) / 2
        new_cy = (self.cy + other.cy) / 2
        return Circle(new_radius, new_cx, new_cy)
    
    

if __name__ == "__main__":
    c1 = Circle(10)
    print( c1 )
    c2 = Circle(5)

    if(c1 == c2): print("They are the same")
    else: print("They are different")

    print("c1 is greater than c2: {}".format( c1 > c2 ) )
    print("c1 is greater or equal than c2: {}".format( c1 >= c2) )
    print("c1 is less than c2: {}".format( c1 < c2 ) )
    print("c1 is less or equal than c2: {}".format( c1 <= c2) )
    
    c3 = c1 + c2
    print( c3 )