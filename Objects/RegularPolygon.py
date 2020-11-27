from math import pi, sin, cos

class RegularPolygon:
    def __init__(self, radius: float, n: int, cx: float, cy: float):
        self.radius = radius
        self.n = n
        self.cx = cx
        self.cy = cy

    @property
    def n(self) -> int:
        return self._n
    @n.setter
    def n(self, n:int) -> None:
        if(n < 3 or type(n) != int): raise ValueError("n must be a integer greater than 2...")
        self._n = n

    @property
    def radius(self) -> float:
        return self._radius
    @radius.setter
    def radius(self, radius: float) -> None:
        if(radius <= 0): raise ValueError("radius must not be negative...")
        self._radius = radius

    def perimeter(self):
        return self.n * self.radius * 2 * sin( pi / self.n )

    def area(self):
        return self.n * self.radius**2 * sin( pi / self.n ) * cos( pi / self.n )

    def __str__(self):
        return f"Radius: {self.radius}, N: {self.n}, Center: ( {self.cx}, {self.cy} ), Perimeter: {self.perimeter()}, Area: {self.area()}"

if __name__ == "__main__":
    p1 = RegularPolygon(5, 6, 0, 0)
    print(p1)