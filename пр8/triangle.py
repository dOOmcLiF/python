def printSides(a, b, c):
    print(f"Стороны равны: {a, b, c}")

def calculatePerimeter(a, b, c):
    perimeter = a + b + c
    return perimeter

def calculateSquare(a, b, c):
    perimeter = calculatePerimeter(a, b, c)
    halfPerimeter = perimeter / 2
    halfPerimeterA = halfPerimeter - a
    halfPerimeterB = halfPerimeter - b
    halfPerimeterC = halfPerimeter - c
    square = (halfPerimeter * halfPerimeterA * halfPerimeterB * halfPerimeterC) ** 0.5
    return square

def calculateHeights(a, b, c):
    square = calculateSquare(a, b, c)
    heightA = 2 * square / a
    heightB = 2 * square / b
    heightC = 2 * square / c
    return heightA, heightB, heightC

def isTriangleExist(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False