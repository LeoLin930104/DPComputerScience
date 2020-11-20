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
    
    def __eq__( self, other ):
        return ( self.radius == other.radius ) and ( self.cx == other.cx ) and ( self.cy == other.cy )

if __name__ == "__main__":
    c1 = Circle(10)
    print( c1 )
    c2 = Circle(10)

    if(c1 == c2):
        print("They are the same")
    else:
        print("They are different")
