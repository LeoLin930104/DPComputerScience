class Rectangle:
    def __init__(self, width: float, length: float, cx: float, cy: float):
        self.width = width
        self.length = length
        self.cx = cx
        self.cy = cy
    
    def area(self) -> float:
        return self.width * self.length
    
    def perimeter(self) -> float:
        return ( self.width + self.length ) * 2

    def __str__(self):
        return f"Width: {self.width}, Length: {self.length}, Area: {self.area()}, Perimeter: {self.perimeter()}, Cx: {self.cx}, Cy: {self.cy}"

if __name__ == "__main__":
    r1 = Rectangle(10, 5, 0, 0)
    print( r1 )
