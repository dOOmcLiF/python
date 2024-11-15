import sys
import triangle

a, b, c = map(int, input().split())

exist = triangle.isTriangleExist(a, b, c)
if exist:
    print("Треугольник существует")
if not exist:
    print("Треугольник не существует")
    sys.exit()

triangle.printSides(a, b, c)

perimeter = triangle.calculatePerimeter(a, b, c)
print(f"Периметр равен: {perimeter}")

square = triangle.calculateSquare(a, b, c)
print(f"Площадь равна: {square}")

heights = triangle.calculateHeights(a, b, c)
print(f"Высоты равны: {heights}")

