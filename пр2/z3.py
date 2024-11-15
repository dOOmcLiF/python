def to_octal(n):
    if n < 0:
        return '-' + to_octal(-n)
    elif n < 8:
        return str(n)
    else:
        return to_octal(n // 8) + str(n % 8)

N = int(input())
print(to_octal(N))