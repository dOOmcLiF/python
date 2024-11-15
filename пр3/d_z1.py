input_data = input()

numbers = list(map(int, input_data.split()))

print(" ".join(map(str, numbers[::2])))