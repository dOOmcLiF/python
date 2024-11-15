class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def printSides(self):
        print(f"Стороны равны: {self.a, self.b, self.c}")

    def calculatePerimeter(self):
        return self.a + self.b + self.c

    def calculateSquare(self):
        perimeter = self.calculatePerimeter()
        halfPerimeter = perimeter / 2
        halfPerimeterA = halfPerimeter - self.a
        halfPerimeterB = halfPerimeter - self.b
        halfPerimeterC = halfPerimeter - self.c
        square = (halfPerimeter * halfPerimeterA * halfPerimeterB * halfPerimeterC) ** 0.5
        return square

    def calculateHeights(self):
        square = self.calculateSquare()
        heightA = 2 * square / self.a
        heightB = 2 * square / self.b
        heightC = 2 * square / self.c
        return heightA, heightB, heightC

    def isTriangleExist(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a
