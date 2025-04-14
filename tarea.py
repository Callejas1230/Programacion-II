class A:
    def __init__(self, x: int, z: int):
        self.x = x
        self.z = z

    def incrementaXZ(self):
        self.x += 1
        self.z += 1

    def incrementaZ(self):
        self.z += 1


class B:
    def __init__(self, y: int, z: int):
        self.y = y
        self.z = z

    def incrementaYZ(self):
        self.y += 1
        self.z += 1

    def incrementaZ(self):
        self.z += 1


class D(A, B):
    def __init__(self, x: int, y: int, z_a: int, z_b: int):
        A.__init__(self, x, z_a)
        B.__init__(self, y, z_b)

    def incrementaXYZ(self):
        self.x += 1
        self.y += 1
        self.z += 1


x = 5
z_a = 20
y = 10
z_b = 10

d = D(x, y, z_a, z_b)

print(f"x = {d.x}, y = {d.y}, z(A) = {d.z}, z(B) = {d.z}")

d.incrementaXYZ()
print(f"x = {d.x}, y = {d.y}, z(A) = {d.z}, z(B) = {d.z}")
