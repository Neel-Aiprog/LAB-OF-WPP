import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def angle_with_x_axis(self):
        return math.degrees(math.atan2(self.y, self.x))

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def cross_product(self, other):
        return self.x * other.y - self.y * other.x

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"


class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        cx = self.y * other.z - self.z * other.y
        cy = self.z * other.x - self.x * other.z
        cz = self.x * other.y - self.y * other.x
        return Vector3D(cx, cy, cz)

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"


v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print("2D Vector Operations:")
print("Magnitude of v1:", v1.magnitude())
print("Angle with X-axis:", v1.angle_with_x_axis())
print("Dot Product:", v1.dot_product(v2))
print("Cross Product:", v1.cross_product(v2))
print("Distance between v1 and v2:", v1.distance_to(v2))

v3d_1 = Vector3D(1, 2, 3)
v3d_2 = Vector3D(4, 5, 6)

print("\n3D Vector Operations:")
print("Magnitude of v3d_1:", v3d_1.magnitude())
print("Dot Product:", v3d_1.dot_product(v3d_2))
print("Cross Product:", v3d_1.cross_product(v3d_2))
print("Distance between v3d_1 and v3d_2:", v3d_1.distance_to(v3d_2))
