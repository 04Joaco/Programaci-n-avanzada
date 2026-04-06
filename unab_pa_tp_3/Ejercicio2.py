class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eje_x(self):
        return self.x

    def eje_y(self):
        return self.y

    def impresion(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def opuesto(self):
        nuevo = Punto(self.x * -1, self.y * -1)
        return nuevo

# =============== prueba

  p1 = Punto(2, 3)

print(p1.impresion())

p2 = p1.opuesto()
print(p2.impresion())

print(p1.eje_x())
print(p1.eje_y())
