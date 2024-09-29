class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Position({self.x}, {self.y})"

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Position(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Position(self.x / other, self.y / other)

    def __floordiv__(self, other):
        return Position(self.x // other, self.y // other)

    def __mod__(self, other):
        return Position(self.x % other, self.y % other)

    def __lt__(self, other):
        return self.x < other.x or (self.x == other.x and self.y < other.y)

    def __le__(self, other):
        return self.x <= other.x or (self.x == other.x and self.y <= other.y)

    def __gt__(self, other):
        return self.x > other.x or (self.x == other.x and self.y > other.y)

    def __ge__(self, other):
        return self.x >= other.x or (self.x == other.x and self.y >= other.y)

    def __neg__(self):
        return Position(-self.x, -self.y)

    def __abs__(self):
        return Position(abs(self.x), abs(self.y))

    def __iter__(self):
        return iter((self.x, self.y))