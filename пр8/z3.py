import pickle
import shelve
from triangle import Triangle

triangles = [
    Triangle(3, 4, 5),
    Triangle(6, 8, 10),
    Triangle(5, 12, 13)
]

with open('triangles.txt', 'w') as file:
    for triangle in triangles:
        file.write(f"{triangle.a},{triangle.b},{triangle.c}\n")

new_triangles = [
    Triangle(7, 24, 25),
    Triangle(8, 15, 17)
]

with open('triangles.txt', 'a') as file:
    for triangle in new_triangles:
        file.write(f"{triangle.a},{triangle.b},{triangle.c}\n")

with open('triangles.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        a, b, c = map(float, line.strip().split(','))
        triangle = Triangle(a, b, c)
        print(f"Стороны треугольника (readline): {triangle.a}, {triangle.b}, {triangle.c}")

with open('triangles.txt', 'r') as file:
    data = file.read()
    lines = data.split('\n')
    for line in lines:
        if line:
            a, b, c = map(float, line.strip().split(','))
            triangle = Triangle(a, b, c)
            print(f"Стороны треугольника (read): {triangle.a}, {triangle.b}, {triangle.c}")

with open('triangles.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        a, b, c = map(float, line.strip().split(','))
        triangle = Triangle(a, b, c)
        print(f"Стороны треугольника (readlines): {triangle.a}, {triangle.b}, {triangle.c}")

with open('triangles.pkl', 'wb') as file:
    pickle.dump(triangles, file)

with open('triangles.pkl', 'rb') as file:
    loaded_triangles = pickle.load(file)
    for triangle in loaded_triangles:
        print(f"Стороны треугольника (pickle): {triangle.a}, {triangle.b}, {triangle.c}")

with open('triangles_separate.pkl', 'wb') as file:
    for triangle in triangles:
        pickle.dump(triangle, file)

with open('triangles_separate.pkl', 'rb') as file:
    while True:
        try:
            triangle = pickle.load(file)
            print(f"Стороны треугольника (pickle по отдельности): {triangle.a}, {triangle.b}, {triangle.c}")
        except EOFError:
            break

with shelve.open('triangles.db') as db:
    for i, triangle in enumerate(triangles):
        db[f'triangle_{i}'] = triangle

with shelve.open('triangles.db') as db:
    for key in db:
        triangle = db[key]
        print(f"Стороны треугольника (shelve): {triangle.a}, {triangle.b}, {triangle.c}")

with shelve.open('triangles.db') as db:
    db['triangle_0'] = Triangle(4, 5, 6)


with shelve.open('triangles.db') as db:
    del db['triangle_0']
