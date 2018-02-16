import math

class Vector2d:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

        if hasattr(x, "__getitem__"):
            x, y = x
            self._v=[float(x), float(y)]
        else:
            self._v=[float(x), float(y)]

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    def fromPoints(p1, p2):
        return Vector2d(p2[0] - p1[0], p2[1] - p1[1])
    def mag(self):
        return math.sqrt(self.x**2 + self.y**2)
    def normalize(self):
        magg = self.mag()
        try:
            self.x/=magg
            self.y/=magg
        except ZeroDivisionError:
            self.x=0
            self.y=0
    def check(self, boundx, boundy):
        if self.x < 0:
            self.x = boundx
        elif self.x > boundx:
            self.x = 0
        if self.y < 0:
            self.y = boundy
        elif self.y > boundy:
            self.y = 0
    def __add__(self, othr):
        return Vector2d(self.x + othr.x, self.y + othr.y)
    def __sub__(self, othr):
        return Vector2d(self.x - othr.x, self.y - othr.y)
    def __neg__(self):
        return Vector2d(-self.x, -self.y)
    def __mul__ (self, val):
        return Vector2d(self.x*val, self.y*val)
    def __truediv__(self, val):
        return Vector2d(self.x/val, self.y/val)
    def __getitem__(self, index):
        return self._v[index]
    def __setitem__(self, index, value):
        self._v[index] = 1.0*value
