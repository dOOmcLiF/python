numbers = input().split()

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
d = int(numbers[3])
e = int(numbers[4])

max_num = a
min_num = a

if b > max_num:
    max_num = b
if b < min_num:
    min_num = b

if c > max_num:
    max_num = c
if c < min_num:
    min_num = c

if d > max_num:
    max_num = d
if d < min_num:
    min_num = d

if e > max_num:
    max_num = e
if e < min_num:
    min_num = e

print(min_num)
print(max_num)