from RegularPolygon import RegularPolygon


class Pentagon(RegularPolygon):
    def __init__(self, radius: float, cx: float, cy: float):
        super().__init__(radius=radius, n=5, cx=cx, cy=cx)


if __name__ == "__main__":
    p1 = Pentagon(5, 0, 0)
    print(p1)