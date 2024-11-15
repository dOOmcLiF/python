N = int(input())

powers_of_two = [2 ** i for i in range(1, N + 1)]

print(*powers_of_two[::-1])
