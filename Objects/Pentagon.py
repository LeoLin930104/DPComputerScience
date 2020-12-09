from RegularPolygon import RegularPolygon

class Pentagon(RegularPolygon):
    def __init__(self, r: float, cx: float, cy: float):
        super().__init__(r = r, n = 5, cx = cx, cy = cx)