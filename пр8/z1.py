import sys
import triangle

a, b, c = map(int, input().split())

trangl = triangle.Triangle(a, b, c)

exist = trangl.isTriangleExist()
if exist:
    print("Треугольник существует")
if not exist:
    print("Треугольник не существует")
    sys.exit()

trangl.printSides()

perimeter = trangl.calculatePerimeter()
print(f"Периметр равен: {perimeter}")

square = trangl.calculateSquare()
print(f"Площадь равна: {square}")

heights = trangl.calculateHeights()
print(f"Высоты равны: {heights}")

